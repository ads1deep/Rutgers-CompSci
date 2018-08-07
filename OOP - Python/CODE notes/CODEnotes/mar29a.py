class Employee:
    def __init__(self, fullname, job_desc, init_pay):
        self.firstname = fullname.split()[0] 
        self.lname = fullname.split()[-1]
        self.job = job_desc
        self.pay = init_pay
    def lastname(self):
        return self.lname
    def is_manager(self):
        return False
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
    def is_manager(self):
        return True
    def give_raise(self, raise_pct, bonus_pct = 0.01):
        Employee.give_raise(self, raise_pct + bonus_pct)
    def give_bonus(self, bonus_pct):
        Employee.give_raise(self, bonus_pct)

class Department:
    def __init__(self, init_mgr, *other_emps):
        if not init_mgr.is_manager():
            raise Exception("Error: init_mgr is not a Manager")
        self.manager = init_mgr
        self.employees = list(other_emps)
        for e in self.employees:
            if e.is_manager():
                raise Exception("Error: Manager object in other_emps")


