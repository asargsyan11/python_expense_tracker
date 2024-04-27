'''
1. make sure to have a good user interface
2. expenses - amount data category
3. data validation
4. categorization - based on predefined categories

'''
import sys


def print_texts(flag):
    if flag == 1:
        print("Welcome to your personal expense tracker.")
    if flag == 2:
        print("Choose an action..")
        print("1.Show the expenses.")
        print("2.Show the categories.")
        print("3.Add an expense.")
        print("4.Add a new cateory.")
        print("5.Exit.")

def tracker(action, expense_list, categories):

    if action == 1:
        #show the list
        for i, expense in enumerate(expense_list, 1):
            print(f"Expense {i}: ")
            print(f"Amount: {expense['amount']}")
            print(f"Date: {expense['date']}")
            print(f"Category: {expense['category']}")
            print()

    elif action == 2:
        for i in categories:
            print(i)
        print()

    elif action == 3:
        #add an expense
        pass
    elif action == 4:
        #add a new category
        pass
    elif action == 5:
        sys.exit()
    else:
        print("Choose a valid option please.")
    

if __name__ == "__main__":
    categories = ['food', 'transportation', 'fees', 'entertainment']
    expense_list = [{'amount' : 1233, 'date': "12.12.23", 'category': 'food'},
                    {'amount' : 122, 'date':  "12.12.23", 'category': 'fees'}]
    print_texts(1)
    while 1:
        action = eval(input(print_texts(2)))
        tracker(action,expense_list, categories)
    

