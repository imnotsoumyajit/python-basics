# nums=[5,2,1,7,5,4,2,8,7]
# # Add new item to the list
# nums.append(69)#at the end of the list 
# nums.insert(0,10)#at custom position
# print(nums)
# nums.insert(0,10)#at custom position
# print(nums)
# nums.remove(1)#that number
# print(nums)

# print(nums.index(7))#returns the first occurrence of the it or else throws an error 
# print(50 in nums)#returns if it is present or not in boolean(No errors - so it is preferred)
# print(nums.count(7))#returns the number of occurrences 
# nums.reverse()#returns the rev sorted list
# print(nums)
# nums.sort()#returns the sorted list
# print(nums)

# nums.pop()#remove last item
# print(nums)
# nums.clear()#remove all items 
# print(nums)

# # To just copy a list
# nums1=nums.copy()
# nums1.append(78)
# print(nums1)
# print(nums)

# Remove duplicated from a list
list=[1,2,3,2,4,5,6,7,9,3,6]
print(f'The original list : {list}')
list1=[]
for i in list:
    if(i not in list1):
        list1.append(i)
print(f'The Updated list : {list1}')
   