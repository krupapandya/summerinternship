from os import name


def myfunction():
    name ="kru"
    age = 21
    return name,age

myname,myage= myfunction()
print("Name is ", myname)
print("Age is ", myage)
