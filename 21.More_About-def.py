"""
•	Formal arguments
•	Actcul arguments
           *   position
           *   keyword
           *   default value
           *   variable length

"""


def OwnFunc(string):  #! Formal arguments
    print("Hello",string)

OwnFunc("Programmers") #! Actcul arguments

def Func(name,age):
    print(name + "\n", age)

Func("Loosu Paiyan",19) #! position

def func(name,age):
    print(name , age)

func(age=19,name="Loosu Paiyan") #! keyword

def function(name,age=19):  #! default value
    print(name , age)

function(name="Loosu Paiyan",)

def Function(name,age,**others):  #! variable length
    print(name , age ,others)

Function(age=19,name="Loosu Paiyan",yr=2021,work="Programmer")


def add(a,*b):
    for var in b:
        a=a+var
    print(a)

add(10,5,4,3,2,1)
