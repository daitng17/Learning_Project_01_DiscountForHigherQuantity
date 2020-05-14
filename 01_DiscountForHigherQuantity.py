# Learning_Project_01_DiscountForHigherQuantity
# This is my first repository after a week of learning Python.

print("-Your shopping cart-")
unit_price = 19.99
print(f"The unit price is: ${unit_price:,.2f}")
quantity = int(input("Enter the quantity: "))
subtotal = unit_price*quantity

if quantity >= 50:
    subtotal = subtotal - subtotal*0.10
    print(10*"_")
    print(f"Confirmed! 10% discount was applied to your subtotal.")
    print(f"Discounted Subtotal: ${subtotal:,.2f}")
else:
    print("\u0332".join("Subtotal") + f": ${subtotal:,.2f}")
    print(f"Buy from 50 items and get 10% cashback!".upper())
    confirm_quantity = int(input("Confirm the quantity: "))
    print("")
    total = unit_price*confirm_quantity
    if confirm_quantity >= 50:
        total = total - total*0.10
        print(10*"-")
        print(f"Confirmed! 10% discount was applied to your subtotal.")
        print(10*"-")
        print(f"Discounted Subtotal: ${total:,.2f}")

print("Thank you! See you next time!")