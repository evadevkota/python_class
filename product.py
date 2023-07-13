items={"cap":1000, "hat":500,"belt":50,"makeup":300}
total_price=0
while True:
    product=input("which product do you want to order if none than type none")
    if product=="none":
        break
    if product in items:
        print(items[product])
        price=items[product]
        total_price+=price
        print(f"{product} is added to the list and its price is {price}" )
    else:
        print("invalid")
print(f"the total price is{total_price} ")




    
    
    
    
