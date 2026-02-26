# set 

essential_spices = {"cardamom", "ginger", "cinnamon", "clove"}
optional_spices = {"cloves", "ginger", "black pepper"}

all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

common_spices = essential_spices & optional_spices
print(f"All spices: {common_spices}")


only_essential = essential_spices - optional_spices
print(f"only_essential spices: {only_essential}")

# memebership test

print(f"Is 'clove' in essential spices ? {'clove' in essential_spices}")