# Get Gross salary
gross_salary_str=input("Enter gross salary:")
gross_salary_int=int(gross_salary_str)

#Get expenses
expenses_str=input("Enter expenses:")
expenses_int=int(expenses_str)

#Get Subscriptions
subscriptions_str=input("Enter subscriptions:")
subscriptions_int=int(subscriptions_str)
Total_Expenses=subscriptions_int+expenses_int

#Calculate the amount remaining
Amount_remaining= gross_salary_int-Total_Expenses

#Output the amount
print("Amount left is :",Amount_remaining)