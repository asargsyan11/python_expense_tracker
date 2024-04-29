
import sys
from datetime import datetime

def print_texts():
    text = ""
    text += "Choose an action:\n"
    text += "1. Show the expenses\n"
    text += "2. Show the categories\n"
    text += "3. Add an expense\n"
    text += "4. Add a new category\n"
    text += "5. Edit an expense\n"
    text += "6. Remove an expense\n"
    text += "7. Show monthly breakdown\n"
    text += "8. Compare expenditures\n"
    text += "9. Exit\n"
    return text

def show_expenses(expense_list):
    #Show expenses
    if expense_list:
        for i, expense in enumerate(expense_list, 1):
            print(f"Expense {i}: ")
            print(f"Amount: {expense['amount']}")
            print(f"Date: {expense['date']}")
            print(f"Category: {expense['category']}")
            print()
    else:
        print("No expenses recorded yet.")

def edit_expense(expense_list):
    show_expenses(expense_list)
    if expense_list:
        index = int(input("Enter the index of the expense to edit: ")) - 1
        if 0 <= index < len(expense_list):
            expense = expense_list[index]
            print(f"Editing expense: {expense}")
            new_amount = float(input("Enter the new amount: "))
            new_date = input("Enter the new date (dd.mm.yy): ")
            new_category = input("Enter the new category: ")
            expense_list[index] = {'amount': new_amount, 'date': new_date, 'category': new_category}
            print("Expense edited successfully.")
        else:
            print("Invalid expense index.")
    else:
        print("No expenses to edit.")

def remove_expense(expense_list):
    show_expenses(expense_list)
    if expense_list:
        index = int(input("Enter the index of the expense to remove: ")) - 1
        if 0 <= index < len(expense_list):
            removed_expense = expense_list.pop(index)
            print(f"Removed expense: {removed_expense}")
            print("Expense removed successfully.")
        else:
            print("Invalid expense index.")
    else:
        print("No expenses to remove.")

def show_monthly_breakdown(expense_list):
    
    monthly_expenses = {}
    for expense in expense_list:
        # Parse 
        date_obj = datetime.strptime(expense['date'], '%d.%m.%y')
        # Extract year and month from the datetime
        year_month = (date_obj.year, date_obj.month)
        # Add the expense to the month
        if year_month in monthly_expenses:
            monthly_expenses[year_month].append(expense)
        else:
            monthly_expenses[year_month] = [expense]

    # Print
    for year_month, expenses in monthly_expenses.items():
        year, month = year_month
        print(f"Expenses for {month}/{year}:")
        for i, expense in enumerate(expenses, 1):
            print(f"{i}. Amount: {expense['amount']}, Date: {expense['date']}, Category: {expense['category']}")
        print()

def compare_expenditures(expense_list, categories):
    print("Choose a comparison option:")
    print("1. Compare spendings across categories")
    print("2. Compare spendings across months")
    option = int(input("Enter your choice: "))

    if option == 1:
        category_totals = {category: 0 for category in categories}
        for expense in expense_list:
            category_totals[expense['category']] += expense['amount']

        print("Spendings across categories:")
        for category, total in category_totals.items():
            print(f"{category}: {total}")

    elif option == 2:
        monthly_totals = {}
        for expense in expense_list:
            date_obj = datetime.strptime(expense['date'], '%d.%m.%y')
            year_month = (date_obj.year, date_obj.month)
            if year_month in monthly_totals:
                monthly_totals[year_month] += expense['amount']
            else:
                monthly_totals[year_month] = expense['amount']

        print("Spendings across months:")
        for year_month, total in monthly_totals.items():
            year, month = year_month
            print(f"{month}/{year}: {total}")

    else:
        print("Invalid option.")

def tracker(action, expense_list, categories):

    if action == 1:
        # Show expenses
        if expense_list:
            show_expenses(expense_list)
        else:
            print("No expenses recorded yet.")

    elif action == 2:
        # Show categories
        print("Categories:")
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")

    elif action == 3:
        # Add an expense
        expense_amount = float(input('Enter the amount spent: '))
        expense_date = input('Enter the date of the expense (dd.mm.yy): ')
        if len(expense_date) != 8 or expense_date[2] != '.' or expense_date[5] != '.':
            print("Invalid date format. Please use dd.mm.yy.")
            return

        print("Choose a category:")
        for index, category in enumerate(categories, 1):
            print(index, category)
        
        selected_category = categories[int(input("Enter the number of the category: ")) - 1]
        
        new_expense = {'amount': expense_amount, 'date': expense_date, 'category': selected_category}
        expense_list.append(new_expense)
        print("Expense added successfully.")

    elif action == 4:
        # Add a new category
        new_category = input("Enter the name of the new category: ")
        if new_category not in categories:
            categories.append(new_category)
            print("Category added successfully.")
        else:
            print("The category already exists.")

    elif action == 5:
        edit_expense(expense_list)
    elif action == 6:
        remove_expense(expense_list)
    elif action == 7:
        show_monthly_breakdown(expense_list)
    elif action == 8:
        compare_expenditures(expense_list, categories)
    elif action == 9:
        # Exit
        confirmation = input("Are you sure you want to exit? (yes/no): ")
        if confirmation.lower() == 'yes':
            print("Exiting...")
            sys.exit()
        else:
            print("Continuing...")

    else:
        print("Invalid action. Please choose a valid option.")

if __name__ == "__main__":
    categories = ['food', 'transportation', 'fees', 'entertainment', 'others']
    expense_list = []

    print("Welcome to your personal expense tracker.")
    while True:
        try:
            action = int(input(print_texts()))
            tracker(action, expense_list, categories)
        except ValueError:
            print("Invalid input. Please enter a number.")