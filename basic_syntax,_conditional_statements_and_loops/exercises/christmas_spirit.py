qty_of_decorations = int(input())
days_left_until_christmas = int(input())
spirit_points_total = 0
money_needed_total = 0
new_qty = 2
total_qty = qty_of_decorations

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

ornament_set_points = 5
tree_skirt_points = 3
tree_garland_points = 10
tree_lights_points = 17

for days in range(1, days_left_until_christmas + 1):
    if days < 11:
        if days % 2 == 0:
            money_needed_total += ornament_set_price * qty_of_decorations
            spirit_points_total += ornament_set_points

        if days % 3 == 0:
            money_needed_total += (tree_skirt_price + tree_garland_price) * qty_of_decorations
            spirit_points_total += tree_skirt_points + tree_garland_points

        if days % 5 == 0:
            money_needed_total += tree_lights_price * qty_of_decorations
            spirit_points_total += tree_lights_points
            if days % 3 == 0:
                spirit_points_total += 30

    if days % 11 == 0:
        total_qty += new_qty
        if days % 2 == 0:
            money_needed_total += ornament_set_price * total_qty
            spirit_points_total += ornament_set_points

        if days % 3 == 0:
            money_needed_total += (tree_skirt_price + tree_garland_price) * total_qty
            spirit_points_total += tree_skirt_points + tree_garland_points

        if days % 5 == 0:
            money_needed_total += tree_lights_price * total_qty
            spirit_points_total += tree_lights_points
            if days % 3 == 0:
                spirit_points_total += 30

    if days >= 11 and days % 11 != 0:
        if days % 2 == 0:
            money_needed_total += ornament_set_price * total_qty
            spirit_points_total += ornament_set_points

        if days % 3 == 0:
            money_needed_total += (tree_skirt_price + tree_garland_price) * total_qty
            spirit_points_total += tree_skirt_points + tree_garland_points

        if days % 5 == 0:
            money_needed_total += tree_lights_price * total_qty
            spirit_points_total += tree_lights_points
            if days % 3 == 0:
                spirit_points_total += 30

    if days % 10 == 0:
        spirit_points_total -= 20
        money_needed_total += tree_lights_price + tree_skirt_price + tree_garland_price

    if days == days_left_until_christmas and days % 10 == 0:
        spirit_points_total -= 30

print(f"Total cost: {money_needed_total}")
print(f"Total spirit: {spirit_points_total}")
