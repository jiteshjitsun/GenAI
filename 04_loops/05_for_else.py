nameAge = [ ('Jitesh', 26), ('Chings', 23), ('Negi', 29)]

for name, age in nameAge:
    if age <= 20:
        print(f"{name} is older than 25")
else:
    print("No one is older")