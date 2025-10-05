a= int(input ("Enter a number:"))

match a:
    case 1:
        print ("you entered 1")
    case 4:
        print ("you entered 4")
    case 10: 
        print ("you entered 10")
    case _:
        print("your number is not listed")