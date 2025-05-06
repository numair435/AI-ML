def decorator(func):
    def wrapper():
        print("This is decorator")
        func()
        print("End of decorator")

@decorator
def function():
    print("This is function")

def generator():
    i=0
    n=5
    while i<=n:
        yield i
        i+=1
x=generator()
for num in x:
    print(num)