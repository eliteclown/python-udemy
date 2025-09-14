order_amount = int(input("Enter your order value\n"))

delivery_fees = 0 if order_amount>300 else 30

print(f"Your delivery fees is: ${delivery_fees}")