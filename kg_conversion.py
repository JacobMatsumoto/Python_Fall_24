#variables for kg values
kg_value_1 = 7
kg_value_2 = 58.3
kg_value_3 = 450
kg_value_4 = 42

#conversion factor: 1 kg = 2.20462 lb
conversion_factor = 2.20462

#calculate lb for each kg value
lb_1 = kg_value_1 * conversion_factor
lb_2 = kg_value_2 * conversion_factor
lb_3 = kg_value_3 * conversion_factor
lb_4 = kg_value_4 * conversion_factor

#output
print(f"{kg_value_1} kgs is equal to {lb_1:.2f} lbs.")
print(f"{kg_value_2} kgs is equal to {lb_2:.2f} lbs.")
print(f"{kg_value_3} kgs is equal to {lb_3:.2f} lbs.")
print(f"{kg_value_4} kgs is equal to {lb_4:.2f} lbs.")