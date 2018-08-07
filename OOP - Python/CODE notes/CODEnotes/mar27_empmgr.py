class Employee:
    def __init__(self, fullname, job_desc, init_pay):
        self.firstname = fullname.split()[0] 
        self.lname = fullname.split()[-1]
        self.job = job_desc
        self.pay = init_pay
    def lastname(self):
        return self.lname
    def give_raise(self, raise_pct):
        """
        Raise the employee's salary by raise_pct on their full
        salary or 80000, whichever is smaller.
        """
        # self.pay = int(self.pay * (1 + raise_pct))
        self.pay += min(self.pay, 80000) * raise_pct
    def __str__(self):
        return "[Employee: %s %s, %s, $%.2f]"%(self.firstname, self.lname, self.job, self.pay)

class Manager(Employee):
    def __init__(self, fullname, init_pay):
        Employee.__init__(self, fullname, "Manager", init_pay)
    def give_raise(self, raise_pct, bonus_pct = 0.01):
        Employee.give_raise(self, raise_pct + bonus_pct)
    def give_bonus(self, bonus_pct):
        Employee.give_raise(self, bonus_pct)

"""      
john = Employee("John Doe", "Tech Support", 85000)
jane = Manager("Jane Smith", 100000)
mike = Employee("Mike Brown", "Janitor", 40000)

emplist = [mike, jane, john]

for e in emplist:
    e.give_raise(0.05)

for e in emplist:
    print(e)
"""

