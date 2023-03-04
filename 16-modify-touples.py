# the workaround for the problem
z=('hi','hello',10,20,3.0,True,'something')

# We first change the touple to a list
y=list(z)
y[1]="New"

x=tuple(y) #conversion
print(x)

# print(touple)
