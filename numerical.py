b=int(input("Enter the first number"))
c=int(input("Enter the second number"))
d=input("Enter the symbol")

def a(num1,num2,symbol):
    if symbol=="+":
        print(num1+num2)
    elif symbol=="-":
        print(num1-num2)
    elif symbol=="*":
        print(num1*num2)
    else:
        print("invalid symbol")
a(b,c,d)

