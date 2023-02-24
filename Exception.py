# age=int(input('Enter your age : '));
# print(age)
# Here if we enter char like a,b,c,/,... it will give us error 
# To prevent that we handle it 
# it is referred to as an exception 

try:
    age=int(input('Enter your age : '));
    income=int(input('Enter your income : '))
    risk = int(income/age);
    print(f'age : {age}\nrisk : {risk}');
except ValueError:
    # print("What tf are you mate ?!")
    print("Invalid Value, Enter a number");
except ZeroDivisionError:
    print("Come again after a year")