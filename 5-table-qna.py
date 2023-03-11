import random

def gen_random(upper):
    r=random.randint(1,upper)
    return r


a=gen_random(10)
b=gen_random(10)
result=a*b

while True:
    print("Enter 999 to give up")
    ans=int(input("What is "+str(a)+"x"+str(b)+" = "))
    if ans==result:
        print("Well done, That is correct")
        break
    elif ans==999:
        print("Looser")
        break
    else:
        print("Wrong answer, Try again")

