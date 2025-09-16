# Program: Expense Tracker for Oceane Nana
# Author: Orlando Nana

def main():
    # Step 1: Ask user for gross salary
    gross_salary = float(input("Enter your gross salary (after tax): "))

    # Step 2: Ask user for expenses
    expenses = float(input("Enter your total expenses for the month: "))

    # Step 3: Ask user for subscriptions
    subscriptions = float(input("Enter your total subscriptions for the month: "))

    # Step 4 & 5: Evaluate total expenses
    total_expenses = expenses + subscriptions

    # Step 6: Calculate remaining amount
    remaining_amount = gross_salary - total_expenses

    # Step 7: Print result
    print("\nSummary:")
    print(f"Gross Salary: ${gross_salary:.2f}")
    print(f"Total Expenses (including subscriptions): ${total_expenses:.2f}")
    print(f"Amount Remaining: ${remaining_amount:.2f}")

# Run the program
main()
