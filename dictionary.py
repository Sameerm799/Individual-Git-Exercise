dict = {} #estabish dictionary

amount = int(input("Enter desired number of pairs: ")) #prompt user to enter amount of pairs

#for loop ranged by amount set earlier, user will enter key and value based on amount set earlier.
for i in range(amount): 
    key = input("Enter key: ")
    value = input("Enter value for key: ")
    dict[key] = value #store key and value into dictionary 

print(dict) #print dicotnary once values entered