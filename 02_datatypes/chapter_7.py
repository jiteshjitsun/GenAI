# Tuples () -> immutable

masala_spices = ("cardamom", "clove", "cinnamon")

(spice1, spice2, spice3) = masala_spices

print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

ginger_ratio, cardamom_ratio = 2, 1
print(f"Ratio is G :{ginger_ratio} and C: {cardamom_ratio}")

ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print(f"Ratio is G :{ginger_ratio} and C: {cardamom_ratio}")

# membership 

print(f"Is Ginger in masala spices ? {'clove' in masala_spices}")