#define BUFFER_SIZE 1024
int Mutex,Prod,Cons;
unsigned char *buffer;
int *currentBuffSize;


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
void SwapBytes(){
	/*  take every pair of bytes from the buffer and swape them
	*/
	int i;unsigned char c;
	for(i=0;i< BUFFER_SIZE ;i+=2){
		if(i+1 >= *currentBuffSize ) break;
		c=buffer[i];
		buffer[i]=buffer[i+1];
		buffer[i+1]=c;
	}
}
void SwapAndSaveBuffer(FILE *f){
	/*  swap bytes ,and append the data to the output file */
	P(Mutex);
	SwapBytes();
	int s=fwrite(buffer,1,*currentBuffSize,f);
	V(Mutex);
}
void init_buffer(){
		/*   Initialize the buffer and the read data size */
		P(Mutex);
		memset(buffer,0,BUFFER_SIZE);
		*currentBuffSize=0;
		V(Mutex);
}
void ReadNextBuffer(FILE *f){
	/*  read the next BUFFER_SIZE*/
	init_buffer();
	/*  extract data from the jumbled file  and fill in the buffer */
	P(Mutex);
	*currentBuffSize=fread(buffer,1,BUFFER_SIZE,f);
	V(Mutex);
}


void waitConsumerToFinish(){
	/*  Mutex:Prod 
	 *  Wait the consumer to finish and call V(Prod)
	 */
	P(Prod);
}
void NotifyConsumerToStart(){
	/* Mutex Cons
	 * Notify the consumer to start unjumbling the buffer,and save the swaped data to the file
	 */
	V(Cons);
}
void waitProducerToFinish(){
	/*  Mutex:Cons 
	 *  Wait the Producer to read the data,
	 */
	P(Cons);
}
void NotifyProducerToStart(){
	/* Mutex Prod
	 * Notify the Producer to start reading data
	 */
	V(Prod);
}
