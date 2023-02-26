def emoji_converter(message):
    words=message.split(' ')
    emojis = {
        ":)":"😊",
        ":(":"😢",
    }
    output=""
    for i in words:
        output+=emojis.get(i,i)+ " "
    return output

message=input(">")
# result=emoji_converter(message)
print(emoji_converter(message))
