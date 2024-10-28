class Employee():
    def __init__(self, name) -> None:
        self.name = name

    def returnPayment(self) -> float:
        return 0

    def __str__(self) -> str:
        return f'Name: {self.name}'

class Salaried(Employee):
    def __init__(self, name, salary) -> None:
        super().__init__(name)
        self.salary = salary

    def returnPayment(self) -> float:
        return self.salary

    def __str__(self) -> str:
        return f'Name: {self.name} Salary: {self.salary}'

class Hourly(Employee):
    def __init__(self, name, hour_value, hour_qtd) -> None:
        super().__init__(name)
        self.hour_value = hour_value
        self.hour_qtd = hour_qtd

    def returnPayment(self) -> float:
        return self.hour_value * self.hour_qtd * 4.5

    def __str__(self) -> str:
        return f'Name: {self.name} Salary: {self.hour_value * self.hour_qtd * 4.5}'

employees = []

if __name__ == '__main__':
    while (True):
        print('''
              1. Add Salaried Employee
              2. Add Hourly Employee
              3. View payroll
              0. Exit
              ''')
        opt = int(input('Inser a option: '))
        match opt:
            case 1:
                name = str(input('Insert name: '))
                salary = float(input('Insert salary: '))
                employees.append(Salaried(name, salary))
            case 2:
                name = str(input('Insert name: '))
                hour_value = float(input('Insert hour value: '))
                hour_qtd = int(input('Insert hours: '))
                employees.append(Hourly(name, hour_value, hour_qtd))
            case 3:
                total = 0
                for employee in employees:
                    total += employee.returnPayment()
                    print(employee)
                print(f'TOTAL: {total}')
                input()
            case 0:
                break

