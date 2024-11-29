import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.file_name = "expenses.json"
        self.load_data()

    def load_data(self):
        """Load expense data from a file."""
        try:
            with open(self.file_name, 'r') as file:
                self.expenses = json.load(file)
        except FileNotFoundError:
            self.expenses = []
        except json.JSONDecodeError:
            print("Error loading data. Starting with an empty expense list.")

    def save_data(self):
        """Save expense data to a file."""
        with open(self.file_name, 'w') as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self):
        """Add a new expense."""
        try:
            date = input("Enter the date (YYYY-MM-DD): ")
            datetime.strptime(date, '%Y-%m-%d')  # Validate date format
            amount = float(input("Enter the amount spent: "))
            description = input("Enter a brief description: ")
            category = input("Enter the category (e.g., food, transport, etc.): ")
            
            expense = {
                "date": date,
                "amount": amount,
                "description": description,
                "category": category
            }
            self.expenses.append(expense)
            self.save_data()
            print("Expense added successfully!")
        except ValueError:
            print("Invalid input. Please try again.")

    def view_expenses(self):
        """Display all expenses."""
        if not self.expenses:
            print("No expenses recorded.")
            return

        print("\nExpenses:")
        for idx, expense in enumerate(self.expenses, 1):
            print(f"{idx}. Date: {expense['date']}, Amount: {expense['amount']}, \
Description: {expense['description']}, Category: {expense['category']}")

    def monthly_summary(self):
        """Display a summary of monthly expenses."""
        monthly_data = {}

        for expense in self.expenses:
            month = expense['date'][:7]  # Extract YYYY-MM
            monthly_data[month] = monthly_data.get(month, 0) + expense['amount']

        print("\nMonthly Summary:")
        for month, total in sorted(monthly_data.items()):
            print(f"{month}: {total:.2f}")

    def category_summary(self):
        """Display a summary of expenses by category."""
        category_data = {}

        for expense in self.expenses:
            category = expense['category']
            category_data[category] = category_data.get(category, 0) + expense['amount']

        print("\nCategory Summary:")
        for category, total in sorted(category_data.items()):
            print(f"{category}: {total:.2f}")

    def menu(self):
        """Display the main menu."""
        while True:
            print("\nExpense Tracker")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Monthly Summary")
            print("4. Category Summary")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_expense()
            elif choice == '2':
                self.view_expenses()
            elif choice == '3':
                self.monthly_summary()
            elif choice == '4':
                self.category_summary()
            elif choice == '5':
                print("Exiting Expense Tracker. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.menu()
