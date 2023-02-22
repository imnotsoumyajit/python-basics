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
input=input("Enter the Number : ")
output=""
for i in input:
    output+= nums.get(i,"?") + " "
print(output)
    