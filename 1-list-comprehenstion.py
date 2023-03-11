# smaller loc to create a new list from an existing list
fruits=["apples","banana","kiwi","something","mango","anything"]
# new list having letter 'a' in it 

# # Method 1
# newFruits=[]
# for i in fruits:
#     if "a" in i:
#         newFruits.append(i)

# M 2 : List comprehension
# newFruits=[x for x in fruits if "a" in x]
# newFruits=[x for x in fruits if "i" in x]
# newFruits=[x for x in fruits if(x!="something")]
# newFruits=[x.upper() for x in range(10) if x<5]
# newFruits=[x.upper() for x in range(10) if x<5]
newFruits=[x if x!="banana" else "orange" for x in fruits]

print(newFruits)