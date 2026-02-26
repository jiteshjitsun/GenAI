order_amount = int(input("Price ? "))

# print(f"order amount {type(order_amount)}")

delivery_fee = 0 if order_amount > 300 else 30

print(f"order amount {order_amount + delivery_fee}")
