opt=input("which operations do you want?")
a=int(input("Enter any number"))
b=int(input("Enter any number"))
def sum(a,b):
    add=a+b
    return add
def sub(a,b):
    subtract=a-b
    return subtract
def div(a,b):
    divide=a/b
    return divide
def mul(a,b):
    product=a*b
    return product   
if opt=="+":
    print(sum(a,b))
elif opt=="-":
    print(sub(a,b))
elif opt=="/":
    print(div(a,b))
elif opt=="*":
    print(mul(a,b))
else:
    print("Invalid output")

print("Program has ended successfully!!") 