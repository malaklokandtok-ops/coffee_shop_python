menu={"coffee":50,"tea":30,"juice":80,"cake":100}
cart={}
def show_menu():
    print("cofee shop menue")
    for item,price in menu.items():
        print(item,price)
def add_item():
    item=input("inter item name:")
    if item not in menu:
        print("item not found")
        return
    quantity=int(input("inter quantity:"))
    if quantity<=0:
        print("quantity not available")
        return
    if item in cart:
        cart[item]+=quantity
    else:
         cart[item]=quantity
    print("item add to cart")
def remove_item():
    item=input("entar item name to remove:")
    if item in cart:
       del cart[item]
       print("item not found in cart")
       return
def show_cart():
    for item,quantity in cart.items():
        price=menu[item]
        total=price*quantity
        print("item:",item)
        print("quantity:",quantity)
        print("total:",total)
def checkout():
    if not cart:
        print("your cart is empty")
        return
    subtotal=0
    for item,quantity in cart.items():
        subtotal+=menu[item]*quantity
        discount=0
        if subtotal>=300:
            discount=subtotal*0.10
            final_price=subtotal-discount
            print("checkout")
            print("subtotal:",subtotal)
            print("discount:",discount)
            print("final price:",final_price)
while True:
    print("coffee shope")
    print("1.show menu")
    print("2.add item")
    print("3.remove item")
    print("4.show cart")
    print("5.checkout")
    print("6.exit")
 
    choice=input("entar your choice:")
    if choice=="1":
        show_menu()
    elif choice=="2" :
        add_item()
    elif choice=="3":
        remove_item()
    elif choice=="4":
        show_cart()
    elif choice=="5":
        checkout()
    elif choice=="6":
        print("thank you")
        break
    else:
        print("invlide choice")


































