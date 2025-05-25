monthly_income = int(input("enter your monthly income:"))
monthly_expenses = int(input("enter your monthly expenses:"))
monthly_savings = monthly_income - monthly_expenses
print("your monthly savings are $", monthly_savings)
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("projected savings after one year, with interest, is: $", projected_savings)
