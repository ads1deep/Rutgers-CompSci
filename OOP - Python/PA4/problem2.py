"""
Amandeep Singh Ruid 145003464
"""

class Time:
    '''Class to mimic Time using hours and minutes'''
    def __init__(self, init_hr = 12, init_min = 0, init_ampm = "AM"):
        '''Constructor with required arguements'''
        if init_hr < 1 or init_hr > 12:
            raise Exception("Error: Invalid hour for Time object")
        if init_min < 0 or init_min > 59:
            raise Exception("Error: Invalid minute for Time object")
        init_ampm = init_ampm.upper()
        if init_ampm != "AM" and init_ampm != "PM":
            raise Exception("Error: Invalid am/pm flag for Time object")

        self.__hr = init_hr
        self.__min = init_min
        self.__ampm = init_ampm



    def hour(self):
        '''Returns Hours'''
        return self.__hr
    
    def minute(self):
        '''Returns Minutes'''
        return self.__min

    def am_pm(self):
        '''Returns Am or PM'''
        return self.__ampm

    def total_minutes(self):
        '''Returns total minutes from midnight'''
        if(self.__ampm=="AM"):
            return self.__hr%12*60 + self.__min
        else:
            return 12*60 + self.__hr%12*60 + self.__min
        
    def __str__(self):
        '''Gives a sstring representation'''
        if(self.__min<10):
            minStr='0'+str(self.__min)
        else:
            minStr=str(self.__min)
        newStr=str(self.__hr)+':'+str(minStr)+self.__ampm
        return newStr

          
    def __repr__(self):
        '''overloads the repr'''
        if(self.__min<10):
            minStr='0'+str(self.__min)
        else:
            minStr=str(self.__min)
        newStr=str(self.__hr)+':'+str(minStr)+self.__ampm
        return newStr

    def __add__(self, mins):
        '''Overloads + and gives sum of time'''
        minsNow=self.total_minutes()
        minsAfterTime=minsNow+mins
        newHour=int((minsAfterTime-minsAfterTime%60)/60%12)
        newMins=minsAfterTime%60
        if(int(minsAfterTime/720)%2==0):
            ampm='AM'
        else:
            ampm='PM'
        if(newHour==0):
            newHour=12
        return Time(newHour,newMins,ampm)
    
    def __sub__(self, mins):
        '''Overloads - and gives difference'''
        minsNow=self.total_minutes()
        minsBeforeTime=(minsNow-mins)+720
        newHour=int((minsBeforeTime-minsBeforeTime%60)/60%12)
        newMins=minsBeforeTime%60
        if(int(minsBeforeTime/720)%2==1):
            ampm='AM'
        else:
            ampm='PM'
        if(newHour==0):
            newHour=12
        return Time(newHour,newMins,ampm)

    
    def __lt__(self,self2):
        '''Overloads <'''
        minsLeft=self.total_minutes()
        minsRight=self2.total_minutes()
        if(minsRight>minsLeft):
            return True
        else:
            return False

    def __gt__(self,self2):
        '''Overloads > '''
        minsLeft=self.total_minutes()
        minsRight=self2.total_minutes()
        if(minsLeft>minsRight):
            return True
        else:
            return False


    def __le__(self,self2):
        '''Overloads <='''
        minsLeft=self.total_minutes()
        minsRight=self2.total_minutes()
        if(minsLeft<=minsRight):
            return True
        else:
            return False

    def __ge__(self,self2):
        '''Overloads >='''
        minsLeft=self.total_minutes()
        minsRight=self2.total_minutes()
        if(minsLeft>=minsRight):
            return True
        else:
            return False

    def __eq__(self,self2):
        '''Overloads =='''
        minsLeft=self.total_minutes()
        minsRight=self2.total_minutes()
        if(minsLeft==minsRight):
            return True
        else:
            return False


    def __ne__(self,self2):
        '''Overloads !='''
        minsLeft=self.total_minutes()
        minsRight=self2.total_minutes()
        if(minsLeft!=minsRight):
            return True
        else:
            return False

    
def time_interval(T1, T2):
    '''Gives difference in hours and mins'''
    min1=T1.total_minutes()
    min2=T2.total_minutes()
    if(min1<min2):
        newMins=min2-min1
    else:
        newMins=min1-min2
    outMins=newMins%60
    outHours=int((newMins-outMins)/60)
    return (outHours,outMins)

