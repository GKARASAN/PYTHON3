number_1 = input("Enter the number : ")
number_2 = input("Enter the number : ")
try:
    calculate = int(number_1) + int(number_2)
    print(calculate)
except Exception as error:
    print(error)

print("Code is sucessful")