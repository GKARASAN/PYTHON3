def Fibonacci(z):
    a = 0
    b = 1
    if z == 0:
        print(0)
    else:
        print(0)
        print(1)
        for i in range(2,z+1):
            c = a + b
            a = b
            b = c
            print(c)


Fibonacci(5)



"""

01123581321

0 + 1 = 1
1 + 1 = 2
1 + 2 = 3
2 + 3 = 5
3 + 5 = 8
5 + 8 = 13
8 + 13 = 21

"""