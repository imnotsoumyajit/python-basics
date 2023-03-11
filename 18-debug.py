import random

def GenRan(upper):
    r=random.randint(1,upper)
    return r

def main():
    program=True
    n1=GenRan(10)
    n2=GenRan(10)
    result=n1*n2
    while program:
        ans=input(f"What is "+str(n1)+" * "+str(n2)+" = ")

        if (ans.isdigit()):
            if(int(ans)==result):
                print("Correct")
            else:
                print("Incorrect")
        else:
            print("Enter a valid number")

x=10
for i in range(x):
    main()

