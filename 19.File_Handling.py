"""
•	“ r “ - open file for reading (default  mode)
•	“ w “ – used for writing
•	“ x “ – creates file if not exists
•	“ a “ - (append) – add more content at the end
•	“ t “ – text mode(default  mode)
•	“ b “ – binary mode
•	“ + “ – read and write

"""

             #! normal method ,1st type access txt file

# pointer = open("python3.txt","a")
# new_variable = pointer.write("some txt")
# new_variable = pointer.write("\nobject oriented programming system")
# print(new_variable)

pointer = open("python3.txt")
new_variable = pointer.read()
print(pointer.tell())
print(new_variable)

pointer.seek(10)
print(pointer.readline())
pointer.close()




          #! with block method , 2nd type access txt file

with open("python3.txt") as pointer:  #! with open txt file as key store in pointer
    print(pointer.read())  #! pointer access read method print all txt