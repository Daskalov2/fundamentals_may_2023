budget = float(input())
price_1kg_flour = float(input())
price_per_pack_eggs = 0.75 * price_1kg_flour
price_per_liter_milk = 1.25 * price_1kg_flour
price_250_milk = 0.25 * price_per_liter_milk
colored_eggs = 0
loaf = 0
i = 0

while budget > (price_1kg_flour + price_250_milk + price_per_pack_eggs):
    i += 1
    loaf += 1
    colored_eggs += 3
    budget -= price_1kg_flour + price_250_milk + price_per_pack_eggs
    if i % 3 == 0:
        colored_eggs -= loaf - 2
    if budget < (price_1kg_flour + price_250_milk + price_per_pack_eggs):
        break

print(f"You made {loaf} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
