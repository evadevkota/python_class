number= int(input("enter a number"))
def prime(number):
    if number<2:
        return False
    for i in range(2,number):
        if number%i==0:
            return False
    return True
if prime(number):
    print("prime")
else:
    print("not prime")
    