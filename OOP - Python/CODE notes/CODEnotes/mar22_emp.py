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
        Raise the employee's salary by raise_pct 
        """
        self.pay = int(self.pay * (1 + raise_pct))
    def __str__(self):
        return "[Employee: %s %s, %s, $%.2f]"%(self.firstname, self.lname, self.job, self.pay)

