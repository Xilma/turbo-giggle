''' A list a value with multiple sequential values.
'''

names = ["Beverly", "Carol", "Stacy", "Nelly", "Tuffy", 35]
uni = ["MMU", "CUEA", "KU", "ANU", "TUK", "JKUAT", "UoN"]
marks = [1, 4, 8, 34, 38, 96, "02", 18, 40]

print(names)
print(uni)
print(marks)
#List Operations

print(uni[2])
print(uni[0])

#List slicing
print(uni[1:3])
print(uni[:3])
print(uni[1:])
print(uni[:-3])
print(uni[1:-2])

#Joining lists
new_list = [names + uni]
print(new_list)
