   #! just example this loop
   #! this code explaind the break and conitnue

x = 10
while True:
    y = int(input("Enter Your Number : "))
    if x > y:
        print("Try Again")
        continue
    elif x < y:
        print("Try Again")
    elif x == y:
        print("Crt Number")
        break