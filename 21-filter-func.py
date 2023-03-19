# return boolean for each item in a list
 
def prime(x):
    for n in range(2,x):
        if(x%n==0):
            return False
        else :
            return True

inp=int(input("Enter the last number: "))
filtered=filter(prime,range(inp))

print("The Prime numbers in between are ",list(filtered))
    
