# f=open("file.txt","r") #for reading 
#print(f.read()) #the entire thing
#print(f.read(25)) #number of char
# print(f.readline()) # line
# print(f.readline()) # line
# print(f.readline(4)) # line with char

# same thing with loop
# for i in f:
#     print(i)

# read the file
# f=open("file.txt","r")
# print(f.read())
# f.close()

# # add to the file 
# f=open("file.txt","a") # a:-append
# f.write("The new line append")
# f.close()

# read the file
# f=open("file.txt","r")
# print(f.read())
# f.close()

# write the file
# f=open("file.txt","w")
# f.write("The new line written")
# # All the prev content of the file will be removed with write mode 
# f.close()
 
# # read the file
# f=open("file.txt","r")
# print(f.read())
# f.close()

# create a file
# f=open("New.txt","x")
# f=open("NewWW.txt","w") #creates a file if not found
# f.close()

# delete files 
import os
# os.remove("NewWW.txt")
if os.path.exists("NewWW.txt"):
    os.remove("NewWW.txt")
else:
    print("No file found")
