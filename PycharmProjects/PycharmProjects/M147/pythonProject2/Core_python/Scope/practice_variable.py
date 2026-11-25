# LEGB
x = 78  # Global variable
def func():
    x = 86  # non local variable
    def inner():
        x = 56  # local variable
        print(x)
    return inner()
func()
print(x)