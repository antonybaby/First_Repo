age=[12,23,4,5,6]
print (age)
age.append(55)
print(age)
print(age.count(55))

table=[4*i for i in range(1,11)]
print(table)
print("index value" ,table.index(36))
age.sort()
table.extend(age)
print(table)

age.insert(2,100)
print(age)
age.sort()
print("Sorting order ", age)
age.pop()
print(age)
print(len(age))
age.remove(55)
print(age)
age.reverse()
print(age)