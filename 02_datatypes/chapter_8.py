# Mutables -> list (Array)
from operator import itemgetter


ingredients = ["water", "milk", "black tea"]
ingredients.append("sugar")
print(f"Ingrdients are: {ingredients}")

ingredients.remove("water")

print(f"Ingrdients are: {ingredients}")


spices_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spices_options)

print(f"chai: {chai_ingredients}")

chai_ingredients.insert(2, "black tea")
print(f"chai: {chai_ingredients}")

last_added = chai_ingredients.pop()
print(f"{last_added}")
chai_ingredients.reverse()
print(f"chai: {chai_ingredients}")


chai_ingredients.sort()
print(f"chai: {chai_ingredients}")

sugar_levels = [1, 2, 3, 4, 5]
print(f"Maximum level sugar: {max(sugar_levels)}")
print(f"Maximum level sugar: {min(sugar_levels)}")

# operator overloading 
base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor
print(f"liquid mixes: {full_liquid_mix}")

strong_brew = ["black_tea", "jitesh"] * 3
print(f"string brew: {strong_brew}")

raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINN", b"CARD")
print(f"Bytes : {raw_spice_data}")