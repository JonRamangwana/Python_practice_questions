#functions a collection of code

def function1():
    print("A")
    print("A2")
print("outside function")

function1()

#functions can be mapping
def function2(x):
    return 2*x

a = function2(3)

print(a)

def function3(x, y):
    return x + y

e = function3(1, 2)

print(e)

def function4(x):
    print(x)
    print("still this function")
    return 3 * x

f = function4(4)

print(f)

def function5(some_argument):
    print(some_argument)
    print("wd")

function5(4)