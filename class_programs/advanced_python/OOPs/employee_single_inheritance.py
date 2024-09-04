class Employee:
    raise_amount = 1.04
    employees = 0

    def __init__(self, f_name, l_name, e_id, salary):
        print("Employee __init__ method")
        self.f_name = f_name
        self.l_name = l_name
        self.e_id = e_id
        self.salary = salary

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


class Developer(Employee):
    raise_amount = 1.1

    def __init__(self, f_name, l_name, e_id, salary, prog_lang):
        print("I am in the developer init method")
        Employee.__init__(self, f_name, l_name, e_id, salary)
        self.prog_lang = prog_lang

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount


dev_1 = Developer('Anil', 'Para', 803, 2000, 'Java')
dev_2 = Developer('Sunil', 'E', 908, 3000, 'Python')

print("before Developer Raise amount=", Developer.raise_amount)
Developer.raise_amount = 1.5
print("After Developer Raise amount=", Developer.raise_amount)

