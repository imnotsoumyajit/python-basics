nums=[5,2,1,7,5,4,2,8,7]
# Add new item to the list
# nums.append(69)#at the end of the list 
# nums.insert(0,10)#at custom position
print(nums)
nums.insert(0,10)#at custom position
print(nums)
nums.remove(1)#that number
print(nums)

print(nums.index(7))#returns the first occurrence of the it or else throws an error 
print(50 in nums)#returns if it is present or not in boolean(No errors - so it is preferred)
print(nums.count(7))#returns the number of occurrences 

nums.pop()#remove last item
print(nums)
nums.clear()#remove all items 
print(nums)