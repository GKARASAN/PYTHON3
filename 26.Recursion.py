import sys
sys.setrecursionlimit(2000)

i = 0
def Recursion():
    global i
    i = i + 1
    print("Hello Programmer's",i)
    Recursion()

Recursion()