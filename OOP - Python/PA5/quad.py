#Amandeep Singh 145003464

from poly import *

class Quadratic(Polynomial):
    '''class which is subclass of polynomial class'''
    def __init__(self,a,b,c):
        '''constructor'''
        self.coeffs=[c,b,a]

    def addterm(self,coeff,exp):
        '''adds a term'''
        if exp<=2:
            Polynomial.addterm(self,coeff,exp)
        else:
            raise Exception("Unable to add term. not quadratic")

    def __add__(self,other):
        '''overrides addition''''
        other2=Polynomial.__add__(self,other)
        c=other2.coeffs[0]
        b=other2.coeffs[1]
        a=other2.coeffs[2]
        return Quadratic(a,b,c)

    def __sub__(self,other):
        '''sub of quad'''
        other2=Polynomial.__sub__(self,other)
        c=other2.coeffs[0]
        b=other2.coeffs[1]
        a=other2.coeffs[2]
        return Quadratic(a,b,c)
    
    def __mul__(self,other):
        '''mult of quad'''
        other2=Polynomial.__mul__(self,other)
        len_list=len(other2.coeffs)
        i=len_list
        while(1==1):
            if(other2.coeffs[i-1]==0):
                i=i-1
            else:
                break
            
        if(i<=2):
            c=other2.coeffs[0]
            b=other2.coeffs[1]
            a=other2.coeffs[2]
            return Quadratic(a,b,c)
        else:
            return other2
        
    def roots(self):
        '''finds roots of quadratic ''''
        c=self.coeffs[0]
        b=self.coeffs[1]
        a=self.coeffs[2]
        if(a==b and b==c and a==0):
            return [0,0,0]
        elif(a==b and a==0 and c!=0):
            return []
        elif(a==0 and b!=0):
            return [-c/b]
        elif(a!=0 and b*b < 4*a*c):
            return []
        elif(a!=0 and b*b == 4*a*c):
            return [-b/(2*a)]
        else:
            return [(-b + (b*b-4*a*c)**(1/2))/(2*a),(-b - (b*b-4*a*c)**(1/2))/(2*a)]
            
        
        
        
        
        
    
