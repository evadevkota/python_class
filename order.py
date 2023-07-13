pizza={"cheese pizza":1000,
       "chicken pizza":2000,
       "mushroom pizza":4000,
       "veg pizza": 4000}
topping={"extra cheese":500,
         "extra mushroom": 400, 
         "extra chicken":500}
total_price=0
pizza_price=0
top_price=0
while True:
    order=input("what do you want to order type none if you want to exit ")
    
    if order=="none":
        print("have a nice day")
        break
    if  order in pizza:
        print(pizza[order])
        price=pizza[order]
        pizza_price+=price
        print(f"your price for {order} is {price}")
    pizza_topping =input("do you want any extra toping type none if you want to exit")
    

    if pizza_topping=="none":
        print("okay we'll respect your choice")
        break
    if pizza_topping in topping:
        print(topping[pizza_topping])
        topping_price=topping[pizza_topping]
        top_price+= topping_price
        print(f"your {pizza_topping} price is {topping_price}")
        
    else:
        print('invalid output')
    file = open('order.txt','w')
    a=file.write(f"your price for {order} is {price}\n")
    b= file.write(f"your {pizza_topping} price is {topping_price}/n")
    c=file.write(f"your total pizza price is{pizza_price}/n")
    d=file.write(f"your total topping price is{top_price}/n")
    e=file.write(f"yout total price is {total_price}/n")
    print(f"your total pizza price is{pizza_price}/n")
    print(f"your total topping price is{top_price}/niz")
total_price=pizza_price+top_price
print(f"yout total price is {total_price}")


