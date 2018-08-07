#Amandeep Singh Ruid 145003464


from bag import *
'''Uses the objects and method from Bag'''

def remove_item(bagObj,item):
    '''removes item from the input bag object'''
    for value in bagObj.items():
        if value==item:
            countItem=bagObj.count(item)
            for i in range(0,countItem):
                bagObj.erase_one(item)

def remove_repeats(bagObj):
    '''remove repeating elements'''
    for value in bagObj.items():
        countValue=bagObj.count(value)
        for i in range(0,countValue-1):
            bagObj.erase_one(value)

def union(B1,B2):
    '''unions two bag objects'''
    unionBag=Bag()
    for value in B1.items():
        countValue=B1.count(value)
        for i in range(0,countValue):
            unionBag.insert(value)
    for value in B2.items():
        countValue=B2.count(value)
        for i in range(0,countValue):
            unionBag.insert(value)
    return unionBag


def intersection(B1,B2):
    '''finds common elelemtns in 2 bag objects'''
    intersectionBag=Bag()
    all_items=[]
    countIntersection=[]
    for item in B1.items():
        all_items.append(item)
    for item in B2.items():
        all_items.append(item)
    all_items=list(set(all_items))
    for item in all_items:
        countValueB1=B1.count(item)
        countValueB2=B2.count(item)
        countIntersection.append(min(countValueB1,countValueB2))
    for j in range(0, len(all_items)):
        countItem=countIntersection[j]
        for k in range(0,countItem):
            intersectionBag.insert(all_items[j])
    return intersectionBag
        


    
