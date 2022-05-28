#4.Using Global and Local variables in same code by using Function in Python
x = "global"
def function():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)
function()
print(x)