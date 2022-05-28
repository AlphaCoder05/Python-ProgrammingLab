#3 Create a nonlocal variable using Function in Python
def outer():
    x = "local" 
    def inner():
        nonlocal x
        x = "nonlocal" 
        print(" inner:", x)
    inner()
    print("outer:", x)
outer()