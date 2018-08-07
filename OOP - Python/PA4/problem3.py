#Amandeep Singh Ruid 145003464


from problem2 import *
'''Uses time methods'''
class Appointment:
    '''Maintains appointment object with start,end times , location and description'''

    def __init__(self, start_time,end_time, location, what='meeting', notes='none'):
        '''Constructor which checks object restrictions'''
        Tstart=Time(7,0,'AM')
        Tend=Time(9,0,'PM')
        
        if(start_time < Tstart):
            raise Exception("Error: Start Time is early ")
        if(end_time>Tend):
            raise Exception("Error : End Time exceeding")
        if(start_time>end_time):
            raise Exception("Error : End Time greater than start time")
        
                
        self.__start_time = start_time
        self.__end_time = end_time 
        self.__location = location
        self.__what = what
        self.__notes = notes

    def start(self):
        '''Returns Start'''
        return self.__start_time

    def end(self):
        '''Returns end Time'''
        return self.__end_time

    def location(self):
        '''Returns location of meeting'''
        return self.__location

    def description(self):
        '''Returns what is meeting about'''
        return self.__what

    def notes(self):
        '''Returns Notes of meeting'''
        return self.__notes

    def duration(self):
        '''Returns duration'''
        T1=self.start().total_minutes()
        T2=self.end().total_minutes()
        return T2-T1
    
    def conflicts(self,other):
        '''Tells if there is a conflict in 2 meetings'''
        if(self.start()<other.start()):
            if(self.end()>other.start()):
                return True
            else:
                return False
        else:
            if(other.end()>self.start()):
                return True
            else:
                return False
    def __str__(self):
        '''Gives string represenation'''
        strOut=''
        strOut='Start Time : ' + str(self.start())+ '    End Time : ' + str(self.end())  + '     Location : ' + self.__location + '    Agenda : ' + self.__what
        return strOut

    def __repr__(self):
        strOut=''
        strOut='Start Time : ' + str(self.start())+ '    End Time : ' + str(self.end())  + '    Location : ' + self.__location + '    Agenda : ' + self.__what
        return strOut

