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


FTE = FullTimeEmployee(10)

CE = ContractEmployee(10, 2)


def main():
    list1 = [FTE, CE], (Employee)
    for i in list1:
        a = FTE.displayInfo("Tim", "001"), FTE.calculateSalary()
        b = CE.displayInfo("Meow", "002"), CE.calculateSalary()
    return a, b

print(main())