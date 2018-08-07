#include <stdio.h>
#include <stdlib.h>
#include <ucontext.h>
#include <stdbool.h>
#define MEM 8192


int threadCount = 0, eraseCount = 0, maxThreadCount = 2700000;
typedef void *Thread;
typedef void *Semaphore;

// ****** THREAD OPERATIONS ******
// Create a new thread.
Thread ThreadCreate(void(*start_funct)(void *), void *args);

// Yield invoking thread
void ThreadYield(void);

// Join with a child thread
int ThreadJoin(Thread thread);

// Join with all children
void ThreadJoinAll(void);

// Terminate invoking thread
void ThreadExit(void);

// ****** SEMAPHORE OPERATIONS ******
// Create a semaphore
Semaphore SemaphoreInit(int initialValue);

// Signal a semaphore
void SemaphoreSignal(Semaphore sem);

// Wait on a semaphore
void SemaphoreWait(Semaphore sem);

// Destroy on a semaphore
int SemaphoreDestroy(Semaphore sem);

// ****** CALLS ONLY FOR UNIX PROCESS ******
// Create and run the "main" thread
void ThreadInit(void(*start_funct)(void *), void *args);

struct context{
    ucontext_t *context;
    int data;
    bool joinAll;
    bool joinSelf;
    bool completed;
    struct context *next;
    struct context *prev;
    struct context *parent;
    struct context *childHead;
    struct context *childTail;
    struct context *nextSibling;
    struct context *prevSibling;
};
typedef struct context *threadPtr;

struct semaphore{
    int value;
    threadPtr head;
    threadPtr tail;
};
typedef struct semaphore *semaphorePtr;

void showThread (threadPtr t) {
    printf(": %d\t",threadCount);
    printf(": %d\t",eraseCount);
    printf(": %d\t",t->data);
    if (t->parent!=NULL) {
        printf(": %d\t",t->parent->data);
    } else {
        printf("t->parent->data: -1\t");
    }
    if (t->nextSibling!=NULL) {
        printf(": %d\t",t->nextSibling->data);
    } else {
        printf("t->nextSibling->data: -1\t");
    }
    if (t->childHead!=NULL) {
        printf(": %d\t",t->childHead->data);
    } else {
        printf("t->childHead->data: -1     ");
    }
    if (t->next!=NULL) {
        printf(": %d\t",t->next->data);
    } else {
        printf("t->next->data: -1    ");
    }
}

void printThreadTree (threadPtr root) {
    
    showThread(root);
    threadPtr child = (root->childHead);
    while (child) {
        threadPtr grandchild = child;
        printThreadTree(grandchild);
        child = child->nextSibling;
    }
    return;
}

void eraseThread (threadPtr t) {
    printf("eraseThread\n"); 
    showThread(t);
    eraseCount++;
    free(t->context);
    free(t);
    return;
}

int retireThread (threadPtr t) {
    // Cannot retire threads unless all its children threads are retired
    printf("retireThread\n");
    
    showThread(t);
    if (t->parent!=NULL) {
        if (t == t->parent->childHead) {
            // If thread is an only child, then make tail point to NULL
            if (t->nextSibling == NULL) {
                t->parent->childHead = NULL;
                t->parent->childTail = NULL;
            } else {
                // If thread is first child, then make nextSibling the first child
                t->parent->childHead = t->nextSibling;
                t->nextSibling->prevSibling = NULL;
            }
        } else if (t == t->parent->childTail) {
            // If thread is last child, then make prevSibling the last child
            t->parent->childTail = t->prevSibling;
            t->prevSibling->nextSibling = NULL;
        } else {
            // else make the previousSibling point to the nextSibling
            t->prevSibling->nextSibling = t->nextSibling;
            t->nextSibling->prevSibling = t->prevSibling;
        }
    }
    return 0;
}

void eraseTree (threadPtr rootThread) {
    printf("EraseTree\n");
    
    showThread(rootThread);
    while (rootThread->childHead) {
        eraseTree(rootThread->childHead);
    }
    eraseThread(rootThread);
}

void addThreadToParent (threadPtr t, threadPtr parent) {
    // If parent has no children, add thread to childhead of parent
    if (parent->childHead == NULL) {
        parent->childHead = t;
        parent->childTail = t;
        t->prevSibling = NULL;
        t->nextSibling = NULL;
    } else { // else add thread to nextSibling of current last child
        parent->childTail->nextSibling = t;
        t->prevSibling = parent->childTail;
        t->nextSibling = NULL;
        parent->childTail = t;
    }
}

void pushToQueue (threadPtr *t, threadPtr *queueHead, threadPtr *queueTail) {
    if (*t == NULL) {
        printf("Error: Tried to add NULL pointer to Queue! Aborting...\n");
        exit (0);
    }
    if (*queueHead == NULL) {   // Initial condition where ready queue is empty
        (*t)->next = NULL;
        (*t)->prev = NULL;
        *queueHead = (*t);
        *queueTail = (*t);
    } else {                   //
        (*t)->next = NULL;
        (*t)->prev = *queueTail;
        (*queueTail)->next = (*t);   // Add thread to end of queue
        (*queueTail) = (*t);         // Increment tail pointer.
    }
    printf("pushToQueue\n"); 
    showThread(*t);
}

threadPtr popFromQueue (threadPtr *t, threadPtr *queueHead, threadPtr *queueTail) {
    printf("popFromQueue\n"); 
    showThread(*t);
    threadPtr returnThread = *t, nextThread = (*t)->next, prevThread = (*t)->prev;
    if (*t == NULL) {
        printf("Error: Tried to pop NULL thread pointer! Aborting...\n");
        exit (0);
    } else if ((*queueHead) == NULL || (*queueTail) == NULL) {
        printf("Error: Tried to pop from empty Queue! Aborting...\n");
        exit (0);
    } else if ((*queueHead == *queueTail) && ((*t != *queueHead) /*|| ((*t)->next != NULL) || ((*t)->prev != NULL)*/) ) {
        printf("Error: Thread not found in queue! Aborting...\n");
        exit (0);
    } else if (*queueHead == *queueTail) {    // If thread is only element in queue
        *queueHead = NULL;
        *queueTail = NULL;
    } else if (*queueHead == *t) {            // If thread is first element in queue
        *queueHead = (*t)->next;
        (*queueHead)->prev = NULL;
    } else if (*queueTail == *t) {            // If thread is last element in queue
        *queueTail = (*t)->prev;
        (*queueTail)->next = NULL;
    } else {                                // If thread is in middle of queue
        (prevThread)->next = (*t)->next;
        (nextThread)->prev = (*t)->prev;
    }
    returnThread->next = NULL;
    returnThread->prev = NULL;
    return returnThread;
}

bool isOnlyChild (threadPtr child) {
    if (child->parent == NULL) {
        printf("Error: Parent pointer is NULL! Aborting...\n");
        exit(0);
    } else {
        printf("isOnlyChild\n"); 
        showThread(child->parent);
    }
    if (child->parent->childHead == child && child->parent->childTail == child) {
        if (child->nextSibling != NULL || child->prevSibling != NULL) {
            printf("Error: Only Child has a sibling exception! Aborting...\n");
            exit(0);
        } else {
            return true;
        }
    }
    return false;
}

bool findImmChild (threadPtr child, threadPtr parent) {
    threadPtr childIter = parent->childHead;
    for (; childIter != NULL; childIter = childIter->nextSibling) {
        if (childIter == child) {
            return true;
        }
    }
    return false;
}

void initThread (threadPtr t, int threadCount, threadPtr currentThread) {
    t->data = threadCount;
    t->joinAll = 0;
    t->joinSelf = 0;
    t->completed = 0;
    t->parent = currentThread;
    t->childHead = NULL;
    t->childTail = NULL;
    t->nextSibling = NULL;
    t->prevSibling = NULL;
}

threadPtr returnRoot (threadPtr t, threadPtr root) {
    printf("returnRoot\n");
    
    showThread(t);
    if (t == root || t->parent == root) {
        return (t);
    }
    while (isOnlyChild(t) && t->parent->completed) {
        t = t->parent;
    }
    return (t);
}

void checkMalloc (void * ptr) {
    if (ptr == NULL) {
        printf("Error: Out of memory! Aborting...\n");
        exit(0);
    }
    return;
}