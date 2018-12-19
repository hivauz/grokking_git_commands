#decorator
def my_decorator(func):
    def f(x,y=5):
        rv = func(x,y)
        print("inside decorator!")
        return rv
    return f

@my_decorator
def sub(x,y =10):
    return x-y
@my_decorator
def add(x,y=7):
    return x+y

#print('add function using decorator!' , add(10,56))
for _ in range(4):
    print(4)
