def display():
    print("Easy coding")

display()

def myadd():
    a=10
    b=10

    print(a+b)

myadd()

def myaddargs(a,b): #a and b are arguments - positional args, default args and keyword args

    print(a+b)

myaddargs(5,9)

def myaddargs(a,b): # positional args

    print("positional arg -> ",a)
    print("positional arg -> ",b)

myaddargs(5,9)

def myaddargs(a,b=43): # default args
    # for defaults args, the default value should be always at the last

    print("default arg -> ",a)
    print("default arg -> ",b)

myaddargs(9)

def myaddargs(a,b): # keyword args

    print("keyword arg -> ",a)
    print("keyword arg -> ",b)

myaddargs(a=12,b=9)

def myreturnfuc(a,b):
    return a+b

myreturnfuc(5,8)

def localvarfunc(): 
    a,b=3,8   # local variables
    return a+b

print("local variable func --> ",localvarfunc())
#print(a) # This will give error

def globalvarfunc(): # local variables
    global a    # this is global variable, available through out the program
    a = 9
    b = 5 # scope: availability of the variable
    return a+b

print("global variable func --> ",globalvarfunc())
print("local variable a --> ",a)