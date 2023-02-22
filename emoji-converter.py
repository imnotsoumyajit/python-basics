# We use dictionary for this kind of thing that wil map chars to the face
message=input(">")
# we need to cut the string at spaces to get individual chars in a list, eg: Good Morning :)
words=message.split(' ')
# print (words)
# We need the dict now to store the chars
emojis = {
    ":)":"😊",
    ":(":"😢",
}
output=""
for i in words:
    output+=emojis.get(i,i)+ " "
print (output)