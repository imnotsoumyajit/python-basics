# x=lambda a: a+20
# x=lambda a,b: a+b
# print(x(5,25))

# or 
def func(n):
    return lambda a:a*n

doub=func(2)
tripl=func(3)

print(doub(7))
print(tripl(7))