dictionarie = {"Name":"Loosu Paiyan","Age":"19","Work":"Hacker"}
#               key  :   value
print(dictionarie)

'''     #! key, values pairs

print(dictionarie.values()) #! print values
print(dictionarie.keys()) #! print keys
print(dictionarie["Work"]) #! print in work key values
     #! some operations

dictionarie["Aim"] = {"Hacker","Programmer"} #! add in exter dict
print(dictionarie)
print(dictionarie["Aim"]) #! print in Aim key values
dictionarie["Work"] = "Programmer" #! work key change in alternative values
print(dictionarie["Work"]) '''

     #! some methods

dict_1 = dictionarie.copy()
dictionarie.popitem()
print(dictionarie)
dictionarie.pop("Age")
print(dictionarie)
dictionarie.clear()
print(dictionarie)
print(dict_1)

''' 

Method	   -  Description
clear()    -  Removes all the elements from the dictionary
copy()	   -  Returns a copy of the dictionary
fromkeys() -  Returns a dictionary with the specified keys and value
get()	   -  Returns the value of the specified key
items()    -  Returns a list containing a tuple for each key value pair
keys()	   -  Returns a list containing the dictionary's keys
pop()	   -  Removes the element with the specified key
popitem()  -  Removes the last inserted key-value pair
setdefault()- Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()   -  Updates the dictionary with the specified key-value pairs
values()   -  Returns a list of all the values in the dictionary
'''

""" dictionarie have lot of method , you can search Google  """