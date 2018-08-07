class Employee:
    def __init__(self, fname, job_desc, init_pay):
        self.firstname = fname.split()[0]
        self.lname = fname.split()[-1]
        self.job = job_desc
        self.pay = init_pay
    def lastname(self):
        return self.lname
    def salary(self):
        return self.pay
    def give_raise(self, raise_pct):
        self.pay = self.pay * (1 + raise_pct)
    def is_manager(self):
        return False
    def __str__(self):
        return "[Employee: %s %s, %s, %d]"%(self.firstname, self.lname, self.job, self.pay)

class Manager(Employee):
    def __init__(self, fname, init_pay):
        Employee.__init__(self, fname, "Manager", init_pay)
    def give_raise(self, raise_pct, bonus_pct = 0.01):
        Employee.give_raise(self, raise_pct + bonus_pct)
    def is_manager(self):
        return True
    def give_bonus(self, bonus_pct):
        Employee.give_raise(self, bonus_pct)
    def __str__(self):
        return "[Manager: %s %s, %d]"%(self.firstname, self.lname, self.pay)


class Department:
    def __init__(self, mgr, *otheremps):
        if not mgr.is_manager():
            raise Exception("Error (Department constructor): Incorrect manager data")
        self.manager = mgr
        self.employees = list(otheremps)
        for e in self.employees:
            if e.is_manager():
                raise Exception("Department constructor error: Manager object in employee list")
    def addmember(self, new_emp):
        if new_emp.is_manager():
            raise Exception("Department addmember error: Cannot add Manager object")
        if new_emp not in self.employees:
            self.employees.append(new_emp)
    def deletemember(self, old_emp):
        if old_emp in self.employees:
            self.employees.remove(old_emp)
    def changemanager(self, new_mgr):
        if not new_mgr.is_manager():
            raise Exception("changemanager error: incorrect parameter")
        self.manager = new_mgr
    def __str__(self):
        # Since we have __getitem__ and __setitem__ defined, we can use
        # the following for loop to implement this method.
        dept_str = ""
        for e in self:
           dept_str += str(e) + "\n"
        return dept_str
    def give_raises(self, raise_pct, mgr_bonus=0):
        self.manager.give_raise(raise_pct, mgr_bonus)
        for e in self.employees:
            e.give_raise(raise_pct)
    def __getitem__(self, index):
        if index < 0 or index >= len(self):
            raise StopIteration
        if index == 0:
            return self.manager
        return self.employees[index-1]
    def __setitem__(self, index, emp):
        if index < 0 or index >= len(self):
            raise IndexError
        if index == 0:
            self.changemanager(emp)
        else:
            if emp not in self and not emp.is_manager():
                self.employees[index-1] = emp
    def __len__(self):
        return 1 + len(self.employees)
    
        
    
