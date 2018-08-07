class Employee:
    def __init__(self, fname, job_desc, init_pay):
        self.firstname = fname.split()[0]
        self.lname = fname.split()[-1]
        self.job = job_desc
        self.pay = init_pay
    def lastname(self):
        return self.lname
    def give_raise(self, raise_pct):
        self.pay = self.pay * (1 + raise_pct)
    def is_manager(self):
        return False
    def __str__(self):
        return "[Employee: %s %s, %s, $%d]"%(self.firstname, self.lname, self.job, self.pay)

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
        return "[Manager: %s %s, $%d]"%(self.firstname, self.lname, self.pay)

class Department:
    def __init__(self, mgr, *otheremps):
        if not mgr.is_manager():
            raise Exception("Department constructor error: incorrect manager parameter")
        self.manager = mgr
        # Check that there are no Manager objects in otheremps
        for e in otheremps:
            if e.is_manager():
                raise Exception("Department constructor error: Only one manager per Department")
        self.employees = list(otheremps)
        
    def addmember(self, new_emp):
        # Check that new_emp is not a Manager object
        if new_emp.is_manager():
            raise Exception("Department addmember method: Cannot add Manager object")          
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
        dept_str = str(self.manager) +"\n"
        for e in self.employees:
            dept_str = dept_str + str(e) +"\n"
        return dept_str
    def give_raises(self, raise_pct, mgr_bonus=0):
        self.manager.give_raise(raise_pct, mgr_bonus)
        for e in self.employees:
            e.give_raise(raise_pct)
        
