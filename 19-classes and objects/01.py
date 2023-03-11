# class and objects
# class is like an object constructor(Blueprint for objects)

# class Human:
#     x=5  #x is a property and 5 is it's value

# # to use class we declare objects
# # h1 is an object
# h1=Human()
# print(h1.x)

# class cant be empty , but we can do by using pass
# class Hooman:
#     pass



#__init__() is called when our class is being initialized, all classes have this function
class Human:
    # def __init__(self,name,age):
        # self parameters are references to the current instances of the class , used to access variables that belong to the class
    def __init__(anything,name,age):
        anything.name=name
        anything.age=age
        #Object Method | objects contain methods(functions that belong to the object) in them 
        # creating a metod
    def methods(something):
        print ("Hi my name is "+something.name)

h1=Human('Soumyajit',21)
h2=Human('Mandal',22)
# print(h1.name)
# print(h1.age)
h1.methods()

# delete an object
del h1

# h2.methods() 
# Object modification
h1.name="Barry"
h1.age=30
h1.methods()