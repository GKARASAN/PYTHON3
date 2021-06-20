from time import asctime
       #! normal method

def func(name,age):

    print("Name is " + name + ", Age is",age)

func("Loosu Paiyan",19)

       #! f string method

def Func(name,age):

    return f"Name is {name}, Age is {age},\ncurrent time & date {asctime()}"

printer = Func("Loosu paiyan",19)

print(printer)