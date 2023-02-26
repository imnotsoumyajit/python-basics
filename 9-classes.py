# Define new type(like list, dictionary, number, etc..) to model new functions 
# class name must be in pascal convention or like Camel case, ie: XxyYyx
class Point:
    # pass self as parameter if its gonna be empty or else error
    def move(self):
        print("Move")

    def draw(self):
        print("Draw")

#2 lines of space  

# call it like a method and here 'point' is a object
point=Point()

# can assign values 
point.x=1
point.y=2

# can call like this
point.move()
point.draw()
print(point.x)
print(point.y)

# this new object is completely different from 
point2=Point()
# print(point2.x) will give err as it is not defined 
point2.x= 3
point2.y= 4
print(point2.x)
print(point2.y)
