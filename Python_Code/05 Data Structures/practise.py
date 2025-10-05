# convert a dictionary to a list of tuples

def dict_func(b):
    c={a: a*2 for a in range(1,11)}
    d= tuple(c.items())
    return d

z=dict_func(5)
print("return value is .....",type(z),z)

# convert a tuple to a list
def tup_func():
    a=(3,4,5,67)
    b=list(a)
    print(b)
    return b
y=tup_func()
print("retun value of list i s......",y,type(y))