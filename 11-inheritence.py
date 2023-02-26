# To avoid duplication of code 
class Parent:
    def type(self):
        print("Family")


# This child class will inherit all the methods def in parent class
class Dog(Parent):
    def dogSound(self):
        print("Woof Woof nigga")
    # we dont like empty classes in py
    # pass
    # With 'pass' the class can remain empty and valid


class Cat(Parent):
    def catSound(self):
        print("Meow Meow nigga")
        
    # pass

dog1=Dog();
dog1.type()
dog1.dogSound()
cat1=Cat();
cat1.type()
cat1.catSound()
