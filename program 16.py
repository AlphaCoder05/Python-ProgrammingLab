#2.Global variable and Local variable with same name
x = 5
def function():
    x = 10
    print("local x:", x)
function()
print("global x:", x)