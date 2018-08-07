from apr03a import *

jane = Manager("Jane Doe", 100000)
john = Employee("John Brown", "tech support", 80000)
kate = Employee("Kate Smith", "tech support", 75000)
betty = Employee("Betty Zubert", "secretary", 40000)
anne = Employee("Anne Graham", "janitor", 35000)
sam = Employee("Sam Simon", "personal trainer", 50000)

sales = Department(jane, john, kate, betty, anne)

sales.deletemember(kate)

for e in sales:
    print(e)

if kate in sales:
    print(kate, " is in sales")
else:
    print(kate, " is not in sales")

L = [e for e in sales if e.salary() > 50000]
print("")

for l in L:
    print(l)





