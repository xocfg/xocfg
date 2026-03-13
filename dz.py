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

FTE = FullTimeEmployee(int(input()))

CE = ContractEmployee(int(input(), input()))

DE = DistanceEmployee(bool(input()), int(input())

def main():
    list1 = [FTE, CE], (Employee)
    for i in list1:
        a = FTE.displayInfo(f"{input(), input()}), FTE.calculateSalary()
        b = CE.displayInfo(f"{input(), input()}), CE.calculateSalary()
        c = DE.displayInfo(f"{input(), input()}), DE.calculateSalary()
    return a, b, c

print(main())