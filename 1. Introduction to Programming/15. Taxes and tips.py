# Creating constants for taxes and tips

TAXES = 0.05
TIPS = 0.18

# Getting input from user

sum_order = int(input("Enter sum of the order: "))

# Creating three variables: for sum with taxes / with tips, and overall sum, including taxes and tips

sum_taxes = sum_order * TAXES
sum_tips = sum_order * TIPS
overall_sum = sum_order + sum_taxes + sum_tips

print(f"Taxes: ${sum_taxes}\nTips: ${sum_tips}\nOverall: ${overall_sum}")
