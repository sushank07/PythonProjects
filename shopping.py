products={"tv":30000 , "phone":15000 , "laptop":35000 , "ac":32000}
total_bill=0
products_cart={ }
while True:
    for i in products:
        print(i ,"-------->", products[i])
    
    choice=int(input(" 1:buy\n 2:remove product\n 3:clear cart\n 4:bill\n 5:exit\n press choice: "))

    if choice == 1:
        products_name=input("enter product name: ")
        if products_name in products:
            products_quantity=int(input("enter quantity: "))
            total_bill=total_bill+(products[products_name]*products_quantity)
            products_cart[products_name]=products_quantity
            print(f"{products_name} buy successfully\n")
        else:
            print("product not available\n")

    elif choice == 2:
        products_name=input("enter product name u want to remove:")
        if products_name in products_cart:
            total_bill=total_bill-(products_cart[products_name]*products[products_name])
            del products_cart[products_name]
            print(f"{products_name} remove successfully from your cart\n")
        else:
            print("no such product in your cart\n")

    elif choice == 3:
        total_bill=0
        products_cart.clear()
        print("cart clear successfully\n")

    elif choice == 4:
        print("your cart ",products_cart)
        print(f"total bill is ----{total_bill} \n")

    elif choice == 5:
        break



# products={"tv":30000 , "phone":15000 , "laptop":35000 , "ac":32000}
# total_bill=0
# products_cart={ }
# while True:
#     for i in products:
#         print(i ,"-------->", products[i])
    
#     choice=int(input(" 1:buy\n 2:remove product\n 3:show cart\n 4:clear cart\n 5:bill\n 6:exit\n press choice: "))

#     if choice == 1:
#         products_name=input("enter product name: ")
#         if products_name in products:
#             products_quantity=int(input("enter quantity: "))
#             total_bill=total_bill+(products[products_name]*products_quantity)
#             products_cart[products_name]=products_quantity
#             print(f"{products_name} buy successfully\n")
#         else:
#             print("product not available\n")

#     elif choice == 2:
#         products_name=input("enter product name u want to remove:")
#         if products_name in products_cart:
#             total_bill=total_bill-(products_cart[products_name]*products[products_name])
#             del products_cart[products_name]
#             print(f"{products_name} remove successfully from your cart\n")
#         else:
#             print("no such product in your cart\n")
     
#     elif choice == 3:
#         if products_cart:
#             print(f"your cart has {products_cart}\n")
#         else:
#             print("cart is empty\n")

#     elif choice == 4:
#         total_bill=0
#         products_cart.clear()
#         print("cart clear successfully\n")

#     elif choice == 5:
#         print("your cart ",products_cart)
#         print(f"total bill is ----{total_bill} \n")

#     elif choice == 6:
#         break
