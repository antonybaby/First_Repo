a={2,3,4,5,6}
b={3,4,5,9,0}

print("Difference Result...",a.difference(b))
print("Union Result...",a.union(b))
print("intersection Result...",a.intersection(b))
a.add(100)
print(a)
a.discard(0) #does not give error if element is not present
print(a)