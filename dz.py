import abc

class Employee(abc.ABC):

    def displayInfo(self, name, id):
        return name, id

    @abc.abstractmethod
    def calculateSalary(self):
        pass

class FullTimeEmployee(Employee):

    def __init__(self, monthlySalary):
        self.monthlySalary = monthlySalary

    def calculateSalary(self):
        return self.monthlySalary

class ContractEmployee(Employee):

    def __init__(self, hourlyRate, hoursWorked):
        self.hourlyRate = hourlyRate
        self.hoursWorked = hoursWorked

    def calculateSalary(self):
        return self.hourlyRate * self.hoursWorked

class DistanceEmployee(Employee):

    def __init__(self, workvolumedone, dayRate):
        self.workvolumedone = bool(workvolumedone)
        self.dayRate = dayRate

    def calculateSalary(self):
        if self.workvolumedone == True:
            return self.dayRate

FTE = FullTimeEmployee(int(input("FTE earn per month: ")))

CE = ContractEmployee(int(input("CE worked: ")), int(input("CE earn per hour: ")))

DE = DistanceEmployee(bool(input("DE done or not: ")), int(input("DE earn per day: ")))

def main():
    list1 = [FTE, CE, DE], (Employee)
    for i in list1:
        a = FTE.displayInfo(input("FTE name: "), input("FTE code:")), FTE.calculateSalary()
        b = CE.displayInfo(input("CE name: "), input("CE code: ")), CE.calculateSalary()
        c = DE.displayInfo(input("DE name: "), input("DE code:")), DE.calculateSalary()
    return f"FTE: {a}, CE: {b}, DE: {c}"
print(main())