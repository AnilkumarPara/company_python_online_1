# Positional arguments
def greetings(greet_type, name):
    print(f"{greet_type} {name}")


# greetings('Sachin', 'Hello')


# Keyword arguments
# def introduce_my_self(name, designation, company):
#     print(f"I am {name} a {designation} working in {company}")


# introduce_my_self(name='Anil', designation='Team Lead', company='UST')

# default arguments
def performance_appriasal_engineers(salary, hike_percentage, design='Lead'):
    salary = salary + salary * hike_percentage
    print("new salary=", salary)


# performance_appriasal_engineers(200000, 4)
# performance_appriasal_engineers(200100, 5)
# performance_appriasal_engineers(300100, 5)

# Variable length arguments
def add(**kwargs):
    # print(args)
    addition = 0
    for v in kwargs.values():
        addition += v
    print(addition)


# add(2, 3)
# add(a=2, b=3, c=4, d=5)


# add(a=2,b=3)

def introduce_my_self(*args, **kwargs):
    print(args)
    print(kwargs)
    # for k, v in kwargs.items():
    #     print(f"{k} is {v}")


introduce_my_self(2,3,name='Anil',Designation='Lead')
