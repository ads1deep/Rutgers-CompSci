
from mar27_empmgr import Employee
from mar27_empmgr import Manager

def create_emplist(empfilename):
    """
    Read employee data from empfilename and return a list
    of employees

    empfilename: name of data file (a string)
    """ 
    empfile = open(empfilename, 'r')
    E = []
    for line in empfile:
        L = line.split()
        if L[2].lower() == "manager":
            E.append(Manager(L[0] + " " + L[1], int(L[3])))
        else:
            E.append(Employee(L[0] + " " + L[1], L[2], int(L[3])))
    empfile.close()
    return E

def give_raises(emplist, raise_pct):
    """
    Give a raise of raise_pct to every item in emplist

    emplist: A list of employees
    """
    for e in emplist:
        e.give_raise(raise_pct)
    
