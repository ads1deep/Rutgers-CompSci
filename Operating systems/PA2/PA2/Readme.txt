First we have defined a structure containing the time_span , duration and an even_string, 
then we have defined an other structure for the minHeap which contains the first element 
of type of the first structure, and a size which contains the number of elements in the minHeap.

Then we have implemented the functions for necessary to manipulate the minHead(insert ,delete ).

in the Main function wa have created a mutex to protect the shared variables and the minHeap 
structure for insertion and deletion .
and then created a new Thread for printing the event_string
 after a signal is emited(which is when the minimum time_span + time() is the = to now) .
 and then updating the next signal absolute time.
in the main thread we keep waiting for the new event 
,which is an input of [time span, duration, event string]. after the user type in this details , 
we add them to the minHeap , if time_span is the minimun in the heap, then we update the next signal 
absolute time to emit this event (wake_time) which is near in the future,otherwise we don't update
 the wake_time ,which contains the nearest event to emit in the future.

If the user types a negative time_span the program stops the thread and exit.
