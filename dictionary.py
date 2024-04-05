dict = {} #estabish dictionary

def delete():#feature to delete key and its corresponding value
    dkey = input("Enter key: ")
    del(dict[dkey])
    print(dict)

def modify(): #feature to modify the value to the corresponding key
    ckey = input("Enter key: ")
    cvalue = input("Enter new value: ")
    dict[ckey] = cvalue
    print(dict)


amount = int(input("Enter desired number of pairs: ")) #prompt user to enter amount of pairs

#for loop ranged by amount set earlier, user will enter key and value based on amount set earlier.
for i in range(amount): 
    key = input("Enter key: ")
    value = input("Enter value for key: ")
    dict[key] = value #store key and value into dictionary 

print(dict) #print dicotnary once values entered
option = int(input("Enter 1 if you want to delete the entry of a key or Enter 2 if you want to change a value: "))
if option == 1:
    delete()
elif option == 2:
    modify()

