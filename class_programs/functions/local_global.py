a = 10  # global variable

def local_global():
    print(globals())
    a = 5  # local variable
    print("Inside a function a=", a)
    print("Inside a function global a=", globals()['a'])
    a = a + 1
    print("Inside a function after modification a=", a)
    globals()['a'] = 20
    print("Inside a function global after modification a=", globals()['a'])

local_global()
print("Outside a function a=", a)
