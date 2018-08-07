from apr03a import *

if __name__ == "__main__":
    jane = Manager("Jane Doe", 100000)
    john = Employee("John Brown", "tech support", 80000)
    kate = Employee("Kate Smith", "tech support", 75000)
    betty = Employee("Betty Zubert", "secretary", 40000)
    anne = Employee("Anne Graham", "janitor", 35000)
    sam = Employee("Sam Simon", "personal trainer", 50000)

    sales = Department(jane, john, kate, betty, anne)

    sales[3] = sam

    lnames = []
    for e in sales:
        lnames.append(e.lastname())
    lnames.sort()
    print("\nDepartment members sorted by last name: \n")
    for l in lnames:
        print(l)

    print("\nSalary Data: \n")

    for i in range(len(sales)):
        print("%-12s    $%7d"%(sales[i].lastname(), sales[i].salary()))





