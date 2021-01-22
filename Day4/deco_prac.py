def plus(func):
    def inner(*args, **kwargs):
        print(args[1] * 30 + kwargs["one"])
        func(*args, **kwargs)
        print(args[1] * 30 + kwargs["one"])
    return inner

@plus
def printer(msg, marks, *args, **kwargs) :
    print(msg)
printer("Hello", "+", one = "DOH") 