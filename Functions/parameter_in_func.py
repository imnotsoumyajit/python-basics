# def greet(name):
#     print(f'Hey {name} ! SMD MF !')

# print("Start")
# user=input("Enter the name : ")
# greet(user)
# print("End")
def greet(f_name,l_name):
    print(f'Hello there Mr {l_name}')
    print(f'God there are many people named "{f_name}"...holy FUCK !')

f_name=input("Enter the first name : ")
# f="Joe"
l_name=input("Enter the last name : ")
# l="Mama"
# greet(f_name=f_name,l_name=l_name)
greet(f_name,l_name)#positional arguments
# greet(total=50, shipping=4, discount=2.8)#keyword arg **:Always after pos arg 
# ie : 
# greet(f_name="Joe",l_name)# not okay
# greet("Joe",l_name="Mama")#okay

