class Employee:
    raise_amount = 1.04
    employees = 0

    def __init__(self, f_name, l_name, e_id, salary):
        print("__init__ method")
        self.f_name = f_name
        self.l_name = l_name
        self.e_id = e_id
        self.salary = salary
        Employee.employees = Employee.employees + 1

    def display(self):
        print(self.f_name)
        print(self.l_name)
        print(self.e_id)
        print(self.salary)

    def apply_raise(self):
        self.salary = self.salary * self.raise_amount

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @staticmethod
    def is_working_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Anil', 'Para', 803, 2000)
emp_2 = Employee('Sunil', 'E', 908, 3000)

print(emp_1.employees)
print(emp_2.employees)
print(f"raise amount Before= {Employee.raise_amount}")
Employee.set_raise_amount(1.1)
print(f"raise amount After = {Employee.raise_amount}")

emp_1.set_raise_amount(1.2)
print(f"raise amount After = {Employee.raise_amount}")

import datetime
today_date = datetime.date(2024, 8, 30)
print(today_date)
print(emp_1.is_working_day(today_date))
