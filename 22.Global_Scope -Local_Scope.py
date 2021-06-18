
Variable = "Hi"  #! global variable

def Func():

    print(Variable)

Func()

def func():
    variable = "Hello" #! local variable
    print(variable)

func()

def Function():
    global var
    print("global key word")

Function()