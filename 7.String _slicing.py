#! string slicing

Variable = "Hello World"
print(Variable[0:5])
print(Variable[0:])
print(Variable[:11]) #! starting is inculed ending is exculed
print(Variable[0:11])

#! Escope sequences

variable = "Hello"
variable1 = "World!"
print(variable,end=" ")
print(variable1)

print("Hello \nWorld!")
print("Hello \tWorld!")
print("Hello \\World!")