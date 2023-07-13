for a in range(1,10,1):
    opt=input("Which operations do you want?" )
    a=int(input("Enter first number"))
    b=int(input("Enter second number"))
    if opt=="+":
        c=a+b
        print("Your output is",c)
    elif opt=="-":
        c=a-b
        print("Your output is",c)
    elif opt=="*":
        c=a*b
        print("Your output is",c)
    elif opt=="/":
        c=a/b
        print("Your output is",c)
    else:
        print("Invalid output")