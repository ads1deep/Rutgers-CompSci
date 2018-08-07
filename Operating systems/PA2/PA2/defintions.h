
#define LCHILD(x) 2 * x + 1
#define RCHILD(x) 2 * x + 2
#define PARENT(x) (x - 1) / 2
#define MAX_LENGTH 100
#define MAX_LENGTH_SCAN "%100s"
typedef struct node {
    int time_span ;
		int duration;
    char event_string[MAX_LENGTH];
} node ;

typedef struct minHeap {
    int size ;
    node *elem ;
} minHeap ;

void P(int);
void V(int);

minHeap* initMinHeap();
void swap(node *, node *);
void heapify(minHeap *, int );
void buildMinHeap(minHeap *, int *, int );
void insertNode(minHeap *, int,char *,int);
void deleteNode(minHeap *);
int getMaxNode(minHeap *, int);
