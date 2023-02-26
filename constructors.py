#  It is a func that gets called at the time of creating an object 
#  problem with classes wala err solve 
class Point:
    # constructor start
    def __init__(self,x,y):
        self.x=x
        self.y=y
    # constructor end
    def move(self):
        print("Move")
    def draw(self):
        print("Draw")


point=Point(10,20)#vls for x and y 
# err is gone
print(point.x)
point.x=11 #we can also update the value
print(point.x)


# Example 
class Person:
    def __init__(self,name):
        self.name=name
    def greet(self,name):
        print(f'Hello {name}')


name=input("Enter your name : ")
message=Person(name)
message.greet(name)
# print(message.name)