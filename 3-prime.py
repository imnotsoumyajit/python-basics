# numbers=(1,2,3,3)
# print(numbers.count(3))
# Prime numbers or nahh
n=int(input("Enter a number : "))
count=0;
for i in range(2,n):
  if (n%i==0):
    count=1;
if(count):
  print("Not prime")
else:
  print("prime")