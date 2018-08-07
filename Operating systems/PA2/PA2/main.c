#include <stdio.h>
#include <stdlib.h>
#include <sys/ipc.h>
#include <sys/sem.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/shm.h>
#include <sys/wait.h>
#include <time.h>
#include <string.h>
#include <pthread.h>
#include <time.h>
#include "defintions.h"

int Mutex,Mutex2;
pthread_t tid2;
minHeap *hp;
int time_span,duration;
int terminate=0;
time_t wake_time;
char buffer[MAX_LENGTH+1];
void *Thread2_Func(void *args){
	while(!terminate){
	P(Mutex);//A mutex to sync access to the minHeap,Block the access for thread 2
		int current_time=time(NULL);//get the current time
		if(current_time>=wake_time){
			//if it's tim to wake up the thread 2 to do the work then let's do it
			//other wise just wait 
			if(hp->size>0){
				//if there is an element in the heap
				//do the work
				//let's pretend we are doing the work for a duration 
				sleep(hp->elem->duration);
				printf("%d -> %s\n",hp->elem->time_span,hp->elem->event_string);
				deleteNode(hp);//now delete the processed element
				//Then the wake up time
				if(hp->size>0){
					//if there is still an other node, set the wake up time for the next one
					wake_time=time(NULL)+hp->elem->time_span;
				}
			}
		}
	V(Mutex);//A mutex to sync access to the minHeap,resume the access for thread 2 or 1
	}
	pthread_exit(NULL);//exit this thread	
}
int main(int argc,char *argv[]){
	Mutex=semget(IPC_PRIVATE,1,IPC_CREAT|IPC_EXCL|0666);
	semctl(Mutex,0,SETVAL,1);/*  A mutex to protect the access to the minHeap*/
	
	hp = initMinHeap() ;//Init our minHeap 
	//Create a new Thread(2)
	pthread_create(&tid2,NULL,Thread2_Func,NULL	);
	printf("typee in : time_span  duration  event_string  (e.g: 1  2  Hello) or negative integer to stop\n");
	while(1){
		/* loop over all input , until a negative integer is entred*/
		scanf("%d",&time_span);//get the time_span
		if(time_span>=0){
			scanf("%d",&duration);//get the duration
			if(duration<0){
				puts("duration  should be positive, goodbye");
				terminate=1;
				break;
			}
			scanf(MAX_LENGTH_SCAN,buffer);//get the event_string
			P(Mutex);//A mutex to sync access to the minHeap,Block the access for thread 2
				if(hp->size>0 && time_span<hp->elem->time_span){
					/* this is the min time span so let's reset the wakeup time for thread2 to current time+span time */
					wake_time=time(NULL) + time_span;
				}else if(hp->size==0){
					// First one
					wake_time=time(NULL) + time_span;
				}
				// Insert a new elemnt to the minHeap
				insertNode(hp, time_span,buffer,duration);
			V(Mutex);//A mutex to sync access to the minHeap,resume the access for thread 2 or 1
		}else{
			/* we can use negative intger as away to terminate the program*/
			puts("Time span should be positive, goodbye");
			terminate=1;
			break;
		}
	}
	puts("Exit");
	return 0;
}


void P(int semid){
		/*  */
		struct sembuf op;
		op.sem_flg=0;
		op.sem_op=-1;
		op.sem_num=0;
		semop(semid,&op,1);
}
void V(int semid){
		/* */
		struct sembuf op;
		op.sem_flg=0;
		op.sem_op=1;
		op.sem_num=0;
		semop(semid,&op,1);
}
