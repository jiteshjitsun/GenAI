chai_type = "ginger chai"
cutomer_name = "Priya"

print(f"Order for {cutomer_name} : {chai_type} please!")

chai_description = "Aromatic and Bold"

print(f"First word: {chai_description[::2]}")
print(f"Last word: {chai_description[12:]}")
print(f"Reverse word: {chai_description[::-1]}")

label_text = "Chai Spêcial"
ecoded_label = label_text.encode("utf-8")

print(f"Non Encoded label: {label_text}")
print(f"Encoded label: {ecoded_label}")

decoded_label = ecoded_label.decode("utf-8")
print(f"Encoded label: {decoded_label}")