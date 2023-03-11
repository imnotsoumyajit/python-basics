# # to store info that come in key value pair; eg:Customer-name,email,age,id,etc
# # each key is associated to a value 
# customer={
#     "name":"Joe Mama",
#     "age":35,
#     "is_milf":True
#     # each key must be unique
# }
# print(customer["name"])
# # print(customer["namezz"])#will give error
# print(customer.get("name"))
# print(customer.get("birthday"))#wont give an error 
# customer["name"]="Sugma Balls"#we can update too
# print(customer.get("name"))
# print(customer.get("birthday","Aug 4 2001"))#we can add  default value
# customer["birthday"]="June 6 1969"
# print(customer.get("birthday"))#we can add new key value pairs to the dictionary

# ex : 1234 -> one two three four
nums={
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine",
    "0":"Zero",
}
print(nums)
# to access the value
# method 1
x=nums["0"]
print(x)
# method 2
y=nums.get("1")
print(y)
# to update the value
nums["0"]="ZeroUpdated"
print(nums.get("0"))
# to update the dictionary
nums.update({"1":"OneUpdated"})
print(nums)
# Add values to the dictionary
nums["new"]="SomethingNew"
print(nums)
# remove values from the dictionary/list/tuples
nums.pop("new")
print(nums)

# input=input("Enter the Number : ")
# output=""
# for i in input:
#     output+= nums.get(i,"?") + " "
# print(output)
