print("This is working")
choice=int(input("Enter number 1, 2, 3 :"));
if(choice==1):
    i=1;
    while(i<5):
        print(f'This is working and has a value of {i}');
        i+=1;
    print("Out of while");
elif(choice==2):
    print("Why is 2 here ?");
else:
    print("Fuck 3");

