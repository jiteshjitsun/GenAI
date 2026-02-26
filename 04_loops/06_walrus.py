flavours = ["ginger", "masala", "elaichi"]

while (flavour := input("Input what flavor you want!")) not in flavours:
    print(f"Sorry, {flavour} is not available")

print(f"Here is your {flavour} tea")