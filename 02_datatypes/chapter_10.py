# dictionary 

chai_order = dict(type="Masal_chai", size="Large", sugar=2)
print(f"Chai order: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"Recipe base: {chai_recipe['base']}")
print(f"Recipe base: {chai_recipe}")

del chai_recipe["liquid"]

print(f"Recipe base: {chai_recipe}")


# print(f"Is sugar in the order? {'sugar' in chai_order}")

# print(f"Order detaisl (keys): {chai_order.keys()}")
# print(f"Order detaisl (values): {chai_order.values()}")
# print(f"Order detaisl (values): {chai_order.items()}")\

last_item = chai_order.popitem()
print(f"Removed item: {last_item}")

extra_spices = {"cardamon": "crushed", "ginger": "slices"}
chai_recipe.update(extra_spices)

print(f"Updated chai recipe: {chai_recipe}")

chai_size = chai_order.get("size", "No notes")
print(f"is available :  {chai_size}")

# datetime, time, calender, timedalta, arrow dateutil