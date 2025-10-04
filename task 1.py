item1_price=500
item2_price=1000
item3_price=1500
budget=4000
total_cost=item1_price+item2_price+item3_price
print(total_cost)
if total_cost <= budget:
    difference = budget - total_cost
    print(f"The budget is enough. You have {difference} left.")
else:
    difference = total_cost - budget
    print(f"The budget is not enough. You need {difference} more.")