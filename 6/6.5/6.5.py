class Myclass:
    name=""

    def function1(self):
        print("Hello")

    def function2(self,name):
        self.name=name

    def function3(self):
        print("value is ", self.name)

m1 = Myclass()
m1.function1()
m1.function2("kru")
m1.function3()

