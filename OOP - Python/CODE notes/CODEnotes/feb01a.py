"""
Code from lecture on February 1
Author: Suneeta Ramaswami
"""
import math

def sqr(a):
    """Returns the square of a number
    a: a number
    """
    a = a*a
    return a


def squares(lst):
    """Return a list of the squares of numbers in a list

    lst: list of numbers
    """
    for i in range(len(lst)):
        lst[i] = lst[i]**2
    return lst
        
def distance(pt1, pt2):
    """Distance between two points in the plane

    pt1, pt2: points represented as 2-tuples of floats
    """
    x1, y1 = pt1  # unpack the 2-tuple pt1
    x2, y2 = pt2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)
    
    
def area(pt1, pt2, pt3):
    """Compute the area of triangle formed by three points in the plane

    pt1, pt2, pt3: points represented as 2-tuples of floats
    """
    a = distance(pt1, pt2)
    b = distance(pt2, pt3)
    c = distance(pt3, pt1)
    s = (a+b+c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

if __name__=="__main__":
    print("\nI'm running a module called feb01a")
    x = 5
    print("x equals ", x) 
    y = sqr(x)
    print("y equals ", y)
    print("x equals ", x) # Note that integer x is not modified by the sqr function

    z = [3,6,1,5,9,4]
    print("the list z: ", z)
    L = squares(z)
    print("the list L: ", L)
    print("the list z: ", z) # Note that list z was modified by the squares function
    q1 = (0,0)
    q2 = (3,0)
    q3 = (0,4)
    print("area equals", area(q1,q2,q3))
    

    
          

