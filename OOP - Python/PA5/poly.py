#Amandeep Singh 145003464

class Polynomial: #the polynomial class
    '''Polynomial class which support svarious operations'''
    def __init__(self,*termpairs): #initialize coefficeint list
        self.coeffs = []
        coeffs=[]
        powers=[]
        for term in termpairs:
            coeffs.append(term[0])
            powers.append(term[1])
        self.coeffs=[0]*(max(powers)+1)
        for i in range(0,len(coeffs)):
            self.coeffs[powers[i]]=coeffs[i]

    def __str__(self):
        '''Converts to string representation'''
        str_to_display=''
        for i in range(0,len(self.coeffs)):
            if(self.coeffs[i]!=0):
                temp=str(self.coeffs[i])+'*'+'x^'+str(i)+'+'
                if(temp[0]=='-'):
                    str_to_display=str_to_display[:-1]
                str_to_display=str_to_display+ temp.replace('+-','-').replace('*x^0','')
        return str_to_display[:-1]
    

    def __repr__(self):
        '''Returns printable version'''
        str_to_display=''
        for i in range(0,len(self.coeffs)):
            if(self.coeffs[i]!=0):
                temp=str(self.coeffs[i])+'*'+'x^'+str(i)+'+'
                if(temp[0]=='-'):
                    str_to_display=str_to_display[:-1]
                str_to_display=str_to_display+ temp.replace('+-','-').replace('*x^0','')
        return str_to_display[:-1]
    
    def degree(self):
         '''degree of expression'''
        return len(self.coeffs)-1

    def evaluate(self,value):
        '''finds value of polynomial at given input'''
        ret_val=0
        for i in range(0,len(self.coeffs)):
            ret_val+=self.coeffs[i]*(value**i)
        return ret_val

        
    def addterm(self, coeff, exp):
        '''adds a term to polynomial'''
        if(exp<=self.degree()):
            self.coeffs[exp]+=coeff
        else:
            self.coeffs=self.coeffs+[0]*(exp-self.degree())
            self.coeffs[exp]=coeff
  

    def removeterm(self,exp):
        '''removes a term'''
        self.coeffs[exp]=0
        
    def scale(self,s):
        '''multiplies each term by factr s'''
        other=Polynomial((0,self.degree()))
        for i in range(0,len(self.coeffs)):
            other.coeffs[i]=self.coeffs[i]*s
        return other

    def __add__(self,other):
        '''adds 2 polynomials'''
        if(self.degree() >= other.degree()):
            other2=Polynomial((0,self.degree()))
            for i in range(0,other.degree()+1):
                other2.coeffs[i]=self.coeffs[i]+other.coeffs[i]
            for i in range(other.degree()+1,self.degree()+1):
                other2.coeffs[i]=self.coeffs[i]
        else:
            other2=Polynomial((0,other.degree()))
            for i in range(0,self.degree()+1):
                other2.coeffs[i]=self.coeffs[i]+other.coeffs[i]
            for i in range(self.degree()+1,other.degree()+1):
                other2.coeffs[i]=other.coeffs[i]
                
        return other2


    def __sub__(self,other):
        '''subtracts 2 poly'''
        if(self.degree() >= other.degree()):
            other2=Polynomial((0,self.degree()))
            for i in range(0,other.degree()+1):
                other2.coeffs[i]=self.coeffs[i]-other.coeffs[i]
            for i in range(other.degree()+1,self.degree()+1):
                other2.coeffs[i]=self.coeffs[i]
        else:
            other2=Polynomial((0,other.degree()))
            for i in range(0,self.degree()+1):
                other2.coeffs[i]=self.coeffs[i]-other.coeffs[i]
            for i in range(self.degree()+1,other.degree()+1):
                other2.coeffs[i]=-other.coeffs[i]
    
        return other2

    def __mul__(self,other):
        '''multiplies 2 poly'''
        other2=Polynomial((0,self.degree()+other.degree()+1))
        for i in range(0,len(self.coeffs)):
            for j in range(0,len(other.coeffs)):
                other2.coeffs[i+j]+=self.coeffs[i]*other.coeffs[j]
        return other2
                
                
    def __getitem__(self,idx):
        '''retrieves inde'''
        return self.coeffs[idx]
    
    def __setitem__(self,idx,value):
        '''sets index value'''
        if(idx>self.degree()):
            self.addterm(value,idx)
        else:
            self.coeffs[idx]=value

def read_polynomial(polyfilename):
    '''reads polynomial from file and returns it'''
    f=open(polyfilename,'r')
    tuple_list=[]
    while(1):
        line=f.readline()
        if line=='':
            break
        else:
            tuple_list.append((int(line.split()[0]),int(line.split()[1])))
    f.close()
    return Polynomial(*tuple_list)

def arith_ops_polys(P,Q):
    '''applies polynomial operations'''
    print('Degree of P')
    print(P.degree())
    print('Degree of Q')
    print(Q.degree())
    print('P+Q')
    print(P+Q)
    print('P-Q')
    print(P-Q)
    print('P*Q')
    print(P*Q)
            
        
            
     
             
         
         
    
    
