#include "myheader.h"

ucontext_t *rootContext;
threadPtr rootThread = NULL, currentThread = NULL;
threadPtr joinQueueHead = NULL, joinQueueTail = NULL;
threadPtr readyQueueHead = NULL, readyQueueTail = NULL;

void Func(){
	printf("This is a func");
}
int main (void) {
    ThreadInit(&Func,NULL);
    printf("Thread1 create\n");
    currentThread = rootThread;
    currentThread = ThreadCreate(&Func,NULL);
    Thread* someThread = ThreadCreate(&Func,NULL);
    someThread = ThreadCreate(&Func,NULL);
    ThreadCreate(&Func,NULL);
    currentThread = someThread; 
    currentThread = ThreadCreate(&Func,NULL);
    printThreadTree(rootThread);
    printf("PrintComplete\n");
    retireThread(someThread);
    printThreadTree(rootThread);
    printf("PrintComplete\n");
    retireThread(rootThread);
    printf("Completed\n");
    return 0;
}

void ThreadExit (void) {
    printf("ThreadExit\n");
    
    showThread(currentThread);
    threadPtr t = currentThread;
    // Check join queue for parent waiting on self
    if (t->parent == NULL && t != rootThread) {
        printf("Error: Exitting thread has no parent! Aborting...\n");
        exit(0);
    }
    if (t->joinSelf || (t != rootThread && t->parent->joinAll && isOnlyChild(t)) ) {
        popFromQueue(&(t->parent), &joinQueueHead,  &joinQueueTail);
        pushToQueue(&(t->parent), &readyQueueHead, &readyQueueTail);
    }
    if (t->childHead) { // If it has a child, mark thread as complete and end process.
        t->completed = true;
        retireThread(t);    //
    } else {            // else Check if its only child and its parent is marked complete.
        threadPtr temp = t;
        t = returnRoot(t, rootThread);
        retireThread(temp);    // Must come after returnRoot else parent looses info on this thread.
        eraseTree(t);   // and erase the whole tree that was waiting on this child.
    }
    if (readyQueueHead != NULL) {
        currentThread = popFromQueue(&readyQueueHead, &readyQueueHead, &readyQueueTail);
        setcontext(currentThread->context);
    } else {
        if (joinQueueHead != NULL) {
            printf("Error: Ready queue empty before join queue! Aborting...\n");
            exit(0);
        } else {
            setcontext(rootContext);
        }
    }
}

void ThreadJoinAll (void) {
    printf("ThreadJoinAll\n"); 
    showThread(currentThread);
    if (readyQueueHead == NULL) {
        printf("Info: Ready Queue is empty. Abort Join process...\n");
        return;
    }
    if (currentThread->childHead == NULL) {
        printf("Info: Thread has no child threads. Abort Join process...\n");
        return;
    }
    currentThread->joinAll = true;
    ucontext_t *tempContext = currentThread->context;
    pushToQueue(&currentThread, &joinQueueHead, &joinQueueTail);
    currentThread = popFromQueue(&readyQueueHead, &readyQueueHead, &readyQueueTail);
    swapcontext(tempContext, currentThread->context);
    return;
}

int ThreadJoin (Thread thread) {
    printf("ThreadJoin\n"); 
    showThread(currentThread);
    threadPtr t = thread;
    if (thread == NULL) {
        printf("Info: Join called on a NULL thread. Aborting Join process...\n");
        return (-1);
    }
    else if (readyQueueHead == NULL) {
        printf("Info: Ready Queue is empty. Aborting Join process...\n");
        return (-1);
    }
    if (!findImmChild(t, currentThread)) {
        printf("Info: Thread either finished execution or its not an immediate child...\n");
        return (-1);
    }
    // thread is an immediate child of currentThread, add currentThread to joinQueue.
    // and yield to next thread in readyQueue;
    t->joinSelf = true;
    ucontext_t *tempContext = currentThread->context;
    pushToQueue(&currentThread, &joinQueueHead, &joinQueueTail);
    currentThread = popFromQueue(&readyQueueHead, &readyQueueHead, &readyQueueTail);
    swapcontext(tempContext, currentThread->context);
    return 0;
}

void ThreadYield (void) {
    ucontext_t *tempContext = currentThread->context;
    pushToQueue(&currentThread, &readyQueueHead, &readyQueueTail);
    currentThread = popFromQueue(&readyQueueHead, &readyQueueHead, &readyQueueTail);
    swapcontext(tempContext, currentThread->context);
}

Thread ThreadCreate (void(*start_funct)(void *), void *args) {
    if (threadCount == maxThreadCount) {
        printf("Error: Maximum memory allocation exceeded! Aborting...\n");
        exit(0);
    }
    threadPtr t = (threadPtr) malloc(sizeof(struct context));
    checkMalloc((void *)t);
    ucontext_t *contextPtr = (ucontext_t*) malloc(sizeof(ucontext_t));
    checkMalloc((void *)contextPtr);
    getcontext(contextPtr);
    contextPtr->uc_link = 0;
    contextPtr->uc_stack.ss_size=MEM;
    contextPtr->uc_stack.ss_flags=0;
    contextPtr->uc_stack.ss_sp=malloc(MEM);
    checkMalloc((void *)contextPtr->uc_stack.ss_sp);
    makecontext(contextPtr, (void (*) (void))start_funct, 1, args);
    threadCount++;
    initThread (t, threadCount, currentThread);
    t->context = contextPtr;
    if (currentThread != NULL) { // Add all threads except root thread to their parents.
        addThreadToParent (t, currentThread);
    }
    printf("ThreadCreate\n");    
    showThread(t);
    pushToQueue(&t, &readyQueueHead, &readyQueueTail);
    return (Thread) t;
}

void ThreadInit (void(*start_funct)(void *), void *args) {
    rootContext= (ucontext_t *) malloc (sizeof(ucontext_t));
    checkMalloc((void *)rootContext);
    rootThread = ThreadCreate(start_funct, args);
    currentThread = popFromQueue(&readyQueueHead, &readyQueueHead, &readyQueueTail);
    if (swapcontext(rootContext, rootThread->context) == -1) {
        printf("Error: Swap from ThreadInit Failed! Aborting...\n");
        exit(0);
    }
}
/* Semaphores */
int SemaphoreDestroy(Semaphore sem) {
    printf("SemaphoreDestroy\n");    
    showThread(currentThread);
    semaphorePtr s = (semaphorePtr) sem;
    if (s->head != NULL) {
        return -1;
    } else {
        free(s);
        return 0;
    }
}

void SemaphoreWait(Semaphore sem) {
    semaphorePtr s = (semaphorePtr) sem;
    printf("SemaphoreWait\n");    
    showThread(currentThread);
    if (s == NULL) {
        printf("Info: Wait on a NULL semaphore called! Returning...\n");
        return;
    }
    s->value --;
    printf(s->value); printf(s->head);
    if (s->value < 0) {
        ucontext_t *tempContext = currentThread->context;
        pushToQueue(&currentThread, &s->head, &s->tail);
        currentThread = popFromQueue(&readyQueueHead, &readyQueueHead, &readyQueueTail);
        swapcontext(tempContext, currentThread->context);
    }
}

void SemaphoreSignal(Semaphore sem) {
    semaphorePtr s = (semaphorePtr) sem;
    printf("SemaphoreSignal\n");
    
    showThread(currentThread);
    threadPtr t;
    s->value ++;
    printf(": %d\t",s->value);
    printf(s->head);
    if (/*s->value < 0 && */s->head != NULL) {
        t = popFromQueue(&s->head, &s->head, &s->tail);
        pushToQueue(&t, &readyQueueHead, &readyQueueTail);
    }
}

Semaphore SemaphoreInit(int initialValue) {
    printf("SemaphoreInit\n");
    if (initialValue < 0) {
        printf("Error: Init value of semaphore is negative! Aborting...\n");
        return  NULL;
    }
    semaphorePtr s = (semaphorePtr) malloc(sizeof(struct semaphore));
    checkMalloc((void *)s);
    s->value = initialValue;
    s->head  = NULL;
    s->tail  = NULL;
    return (Semaphore) s;
}
