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

#include "definitions.h"

int main(int argc,char *argv[]){
	Mutex=semget(IPC_PRIVATE,1,IPC_CREAT|IPC_EXCL|0666);
	semctl(Mutex,0,SETVAL,1);/*  A mutex to protect the access to buffer*/
	
	Prod=semget(IPC_PRIVATE,1,IPC_CREAT|IPC_EXCL|0666);
	semctl(Prod,0,SETVAL,1);/*  a mutex to controle the execution of the producer*/
	
	Cons=semget(IPC_PRIVATE,1,IPC_CREAT|IPC_EXCL|0666);
	semctl(Cons,0,SETVAL,0);/*  a mutex to controle the execution of the consumer*/
	
	int BufSeg = shmget(IPC_PRIVATE,BUFFER_SIZE, IPC_CREAT|0666);
	buffer = (unsigned char *) shmat(BufSeg, NULL, 0);/*  Shred buffer */
	
	int BufSizeSeg = shmget(IPC_PRIVATE,1*sizeof(int), IPC_CREAT|0666);
	currentBuffSize = (int *) shmat(BufSizeSeg, NULL, 0);/* shared variable containing the size of the last read data (buffer) */
	int pid=fork();
	if(pid==0){
		//Producer
		FILE *f_input=fopen(argv[1],"rb");
		while(1){
			waitConsumerToFinish();

			ReadNextBuffer(f_input);
			
			NotifyConsumerToStart();
			if(*currentBuffSize==0){
				//If there is no data to read,then exit
				break;
			}
		}
		fclose(f_input);
		exit(0);
	}else{
		FILE *f_output=fopen(argv[2],"wb");

		//Consumer

		while(1){
			waitProducerToFinish();
			/* read and swape every pair of bytes in the buffer data and save it to file argv[2] */

			SwapAndSaveBuffer(f_output);
			
			NotifyProducerToStart();
			if(*currentBuffSize==0){
				//If there is no data to read,then exit
				break;
			}
		}
		fclose(f_output);
	}
	while(wait(NULL)>0);
	printf("Unjumbling finished, the data is saved to: %s \n",argv[2]);
	return 0;
}
