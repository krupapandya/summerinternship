from re import X


def my_function():
    X=20
    print("value inside function:", X)

X=40
my_function()
print("value outside function:", X)
