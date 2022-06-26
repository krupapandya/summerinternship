class parentclass():

    def function1(self):
        print("Parent method called")

class Childclass(parentclass):

    def function1(self):
        print("Childclass method called")

c = Childclass()
c.function1()
