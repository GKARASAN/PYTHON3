person_1 = int(input("Enter your point : "))
person_2 = int(input("Enter your point : "))

if person_1 > person_2:
    print("1st person is winner*")
elif person_1 == person_2:
    print("match is draw .. you have same point's")
else:
    print("2nd person is winner*")

""" 

any one contison is true code will be stop in that contison, contison is false run nxt contisons

"""

        #!  short hand if else statement

''' i will not preferred this method, just for knowlage , don't use this method'''

var1 = 1
var2 = 2

print("var2 is greaterthen") if var1 < var2 else print("var1 is less then")