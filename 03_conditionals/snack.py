snack = input("what do you want to order ").lower()

if snack == "samosa" or snack == "cookies":
    print(f"here is your {snack}")
else:
    print("sorry we don't have this item")