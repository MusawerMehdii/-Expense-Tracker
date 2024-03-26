# Function to add an expense to the expenses list
def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    
# Function to print all expenses in the expenses list
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
# Function to calculate the total expenses
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))
    
# Function to filter expenses by a specific category
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)

# Main function to run the expense tracker program
def main():
    expenses = []  # Initialize an empty list to store expenses
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
        
        choice = input('Enter your choice: ')  # Prompt the user for input
        
        # Option 1: Add an expense
        if choice == '1':
            amount = float(input('Enter amount: '))  # Get the amount of the expense
            category = input('Enter category: ')  # Get the category of the expense
            add_expense(expenses, amount, category)  # Call add_expense function

        # Option 2: List all expenses
        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)  # Call print_expenses function to display all expenses

        # Option 3: Show total expenses
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))  # Call total_expenses function to calculate and print total expenses

        # Option 4: Filter expenses by category
        elif choice == '4':
            category = input('Enter category to filter: ')  # Get the category to filter expenses
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)  # Filter expenses by the specified category
            print_expenses(expenses_from_category)  # Print filtered expenses

        # Option 5: Exit the program
        elif choice == '5':
            print('Exiting the program.')
            break  # Exit the loop and end the program
   main()
