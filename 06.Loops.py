# For Loop

a= int(input("Enter number:"))
print ("multiplcation table of ", a)
for i in range(1,11):
    print (i, "X", a,"=",i*a)
print ("end of program")

# While Loop
print("while loop example")
while(a>6):
    print (a)
    a+=1
    if a>10:
        print("loop break")
        break
print ("end of while loop")