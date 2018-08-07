#include <stdio.h>
#include "malloc.h"

#define malloc(x) my_malloc(x, __FILE__ , __LINE__);
#define free(x)   myfree((void*)x, __FILE__ , __LINE__ );

int r_initialized = 0;					//To check if root of myblock is initialized
int l_initialized = 0; 					//To check if last of myblock is initialized
unsigned long int r_allocated   = 0;		//Total small chunks size
unsigned long int l_allocated   = 0; 	//Total big chunks size

/*
 * Malloc function
 * Will return a void pointer to the allocated space
 */
void* my_malloc(unsigned int size,char *file, int line) {
/*
Implement malloc such that the smaller chunks are allocated from the left, with root pointing to the start of chunk.
The bigger chunks are allocated from the right end, with last pointing to the end of the chunk.
Use big to record if the chunk is bigger or smaller (big if size>1000). This reduces fragmentation
*/
	int big=0;

	if(size>(blocksize))	{									//invalid size
		printf("enter size between 0 and 1<<20\n");
		printf("file %s line %d\n",file,line);
		}


	else if((l_allocated+r_allocated+sizeof(mementry)+size+16)>(blocksize)) {	//Saturation condition
		printf("memory full/error \n");
		printf("file %s line %d\n",file,line);
		}
		
	else {
	if(size >1000)												//big chunk
		big=1;

	static mementry *root=NULL;									//mementry poiniting to the start of our block
	static mementry *last=NULL;									//mementry pointing to the end of our block.
    mementry *succ,*prev;										//use to point next and prev mementry to maintain the link between chunks
    mementry *p;												//use this pointer to traverse through myblock
	succ=prev=NULL;

	if(!r_initialized) {          								//if root myblock is not initialized, initialize it.
        root=(mementry*)myblock;                				//point root to start of the block
        root->prev=root->succ=NULL;            				    //initialize the pointers to NULL
        root->size=(blocksize)/2-sizeof(mementry);    			//store the allocatable size for small chunks
        root->recognize=recogpattern;		 					//useful to know while freeing whether we're pointing to a mementry, not random
        root->isfree=1;         								//memory is not allocated
        r_initialized=1;          								//initialization done
       }

   if(!l_initialized) { 											//if last is not initialized
   		last=(mementry*)(myblock+(blocksize)-sizeof(mementry)	//point last to end - size required for the chunk
        					-size);
        last->prev=last->succ=NULL;
        last->size=(blocksize)/2-sizeof(mementry);				//store the allocatable size for big chunks
        last->recognize=recogpattern;
        last->isfree=1;
        l_initialized=1;
   }
   p=root;														//point to start
   if(big==0) {													//SMALL CHUNK
	do  {
		if(p->size<size) 										//if the current chunk is small, skip it, we can't malloc here
			p=p->succ;											//move ahead

		else if(!p->isfree) 									//memory availble, but already allocated
			p=p->succ;											//move ahead

		else if(p->size < (size+sizeof(mementry)+4)) { 			//check if the size requested + mementry overhead size doesnt exceed availble space. Take an extra padding of 4 bytes so as to avoid completely full memory.
			p->isfree=0;									 	//allocate here
			p->recognize=recogpattern;
			return ((char*)p+sizeof(mementry)); 										//malloc returns the address where the data field starts from.
		}

		else {
			succ=(mementry*)((char*)p+sizeof(mementry)+size);	//create mementry for a new chunk
			succ->prev=p;										//link the next mementry's previous to current node
			succ->succ=p->succ;									//link the next of p as succ's next
			if(p->succ!=NULL) 									//if its not the end of heap, point the next node's previous to succ
				p->succ->prev=succ;

			p->succ=succ;										//point p's succ to succ node
			succ->size=p->size-sizeof(mementry)-size;			//out of the original size, subtract mementry and size
			succ->isfree=1;										//once p is used, the remanining (succ) is free
			p->size=size;
			p->recognize=recogpattern;
			p->isfree=0;										//p is allocated now
			return ((char*)p + sizeof(mementry));
		}

	} while(p!=NULL);
 }
 	else														//BIG CHUNK
 		{
 			p=last;
 			do  {
		if(p->size<size) 										//if the current chunk is small, skip it, we can't malloc here
			p=p->succ;											//move ahead

		else if(!p->isfree) 									//memory availble, but already allocated
			p=p->succ;											//move ahead

		else if(p->size < (size+sizeof(mementry)+4)) { 			//check if the size requested + mementry overhead size doesnt exceed availble space. Take an extra padding of 4 bytes so as to avoid completely full memory.
			p->isfree=0;									 	//allocate here
			p->recognize=recogpattern;
			return p+1; 										//malloc returns the address where the data field starts from.
		}

		else {
			succ=(mementry*)((char*)p-sizeof(mementry)-size);	//create mementry for a new chunk
			succ->prev=p;										//link the next mementry's previous to current node
			succ->succ=p->succ;									//link the next of p as succ's next
			if(p->succ!=NULL) 									//if its not the end of heap, point the next node's previous to succ
				p->succ->prev=succ;

			p->succ=succ;										//point p's succ to succ node
			succ->size=(blocksize)/2-sizeof(mementry)-size;		//out of the original size, subtract mementry and size
			succ->isfree=1;										//once p is used, the remanining (succ) is free
			p->size=size;
			p->recognize=recogpattern;
			p->isfree=0;										//p is allocated now
			return ((char*)p+sizeof(mementry));
		}

	} while(p!=NULL);
 		}
 }
return 0;
}

void myfree(void* p, char* file, int line) {
mementry *ptr,*prev,*succ;											//ptr->current chunk prev->previous succ->next
ptr=prev=succ=NULL;

if(!((p-(void*)myblock>=0)&&(p-(void*)myblock<(blocksize)))) {		//check p exists within the chunk
	printf("input is not in the block\n");
	printf("file  %s line %d\n",file,line);
	return;
	}

ptr=(mementry*)p-1;													//point to mementry, not the size field we returned in malloc
			

if((ptr)->recognize!=recogpattern) {								//check if pointer points to a mementry and not random location
	printf("We're not pointing to a chunk\n");
	printf("file %s line %d\n",file,line); 
	return;
	}
	
if(ptr->isfree==1) {												//freeing chunk already freed
	printf("We're trying to free a chunk already freed\n");
	printf("file %s line %d\n",file,line); 
	return;
	}
	
if (ptr->size<1000)													//update the allocated space
		l_allocated-=ptr->size;
else
		r_allocated-=ptr->size;			
	
if((prev=ptr->prev)!=NULL&& prev->isfree) {							//is the previous chunk free as well?
	prev->size+=sizeof(mementry)+ptr->size;							//combine previous and current chunk
	prev->succ=ptr->succ;											//link next pointer over the chunk we are freeing
	if(ptr->succ!=NULL)												//if chunk exists in front, link its prev to previous chunk
		ptr->succ->prev=prev;
	}
	
else {																//previous is not free, just assign prev to current chunk
	ptr->isfree=1;
	prev=ptr;
	}
	
if( (succ=ptr->succ)!=NULL && succ->isfree)							//is succeeding chunk free?
{
	prev->size+=sizeof(mementry)+succ->size;						//combine current and next chunk
	prev->succ=succ->succ;
	if(succ->succ!=NULL)											//link over the current chunk to be freed
		succ->succ=prev;
}	
	printf("freed chunk at address %p\n",p);
	

}

int main ()
{
mementry *A[5];		//example array of mementries
printf ("Chunk starts at %p and ends at %p\n",myblock,myblock+(blocksize));
printf ("Chunk size - %d\n",blocksize);
printf ("Size of mementry structure is %lu\n",sizeof(mementry));
//First Malloc
A[0]=malloc(10100);

if(A[0]!=NULL) {				//malloc check
	l_allocated=l_allocated+10100;
	printf("memory allocated at address %p\n",(void*)A[0]);
	printf("total memory allocated %lu bytes \n",l_allocated+r_allocated);
	}
else
	printf ("malloc failed\n");

//Second Malloc
A[1]=malloc(11010);
if(A[1]!=NULL) {				//malloc check
	r_allocated=r_allocated+11010;
	printf("memory allocated at address %p\n",(void*)A[1]);
	printf("total memory allocated %lu bytes \n",l_allocated+r_allocated);
	}
else
	printf ("malloc failed\n");

//Third Malloc
A[2]=malloc(20);
if(A[2]!=NULL) {				//malloc check
	l_allocated=l_allocated+20;
	printf("memory allocated at address %p\n",(void*)A[2]);
	printf("total memory allocated %lu bytes \n",l_allocated+r_allocated);
	}
else
	printf ("malloc failed\n");

//Fourth Malloc
A[3]=malloc(2020);
if(A[3]!=NULL) {				//malloc check
	r_allocated=r_allocated+2020;
	printf("memory allocated at address %p\n",(void*)A[3]);
	printf("total memory allocated %lu bytes \n",l_allocated+r_allocated);
	}
else
	printf ("malloc failed\n");

free(0);

free(A[0]);
printf("total memory allocated %lu bytes \n",l_allocated+r_allocated);
free(A[3]);
printf("total memory allocated %lu bytes \n",l_allocated+r_allocated);
free(A[3]);
free(A[0]);
return 0;
}

