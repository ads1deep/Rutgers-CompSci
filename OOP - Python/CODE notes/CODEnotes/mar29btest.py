from mar29b import *

jane = Manager("Jane Doe", 100000)
john = Employee("John Brown", "tech support", 80000)
kate = Employee("Kate Smith", "tech support", 75000)
betty = Employee("Betty Zubert", "secretary", 40000)
anne = Employee("Anne Graham", "janitor", 35000)
sam = Employee("Sam Simon", "personal trainer", 50000)
bob = Manager("Bob Brown", 86000)


sales = Department(jane, john, kate, betty, anne)

print(sales)

sales.deletemember(kate)

print(sales)

# sales.addmember(bob)
sales.changemanager(bob)

print(sales)

sales.give_raises(0.03, 0.01)

print(sales)

# for e in sales:
#    print(e.lastname())





