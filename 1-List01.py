# names=['Ram','Sham','Ghoda','Loda','Shoba','Nova']
#        0      1      2       3      4       5
# print(names)
# print(names[2])
# print(names[2:4])
# names[3]='Lorda'#Update the list 
# print(names[2:])

# Largest num in a list
nums=[1,2,4,5,8,4,3]
i=0
gi=nums[0]
for i in nums:
    if(i>gi):
        gi=i;
print(f'The greatest number in the list is : {gi}')
