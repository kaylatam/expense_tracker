import sqlite3
import matplotlib as plt
import datetime
import re
import unittest


class Expense:
    """Simple program to help the user keep track of their budget"""

    def __init__(self, db="expense.db"):
        """Setting up the db and initializing variables"""

        # Setting up income, savings, and budget to be 0
        self.income = 0
        self.savings = 0
        self.budget = 0

        # Connect to expense database
        self.connection = sqlite3.connect(db)

        # Basis for individual actions
        self.cursor = self.connection.cursor()

    def display_menu(self):
        """Asks the user what they would like to do"""

        print("Please select what you would like to do")
        # Adds expense entry
        print("1. Add expense")
        # Deletes an expense entry
        print("2. Delete expense")
        # Lets the user their expenses by month and year
        print("3. View Expenses")
        # Lets the user see their current budget left
        print("4. Current budget")
        # Lets the user add to their current budget
        print("5. Add to budget")

    def update_income(self):
        """Prompts user for their income"""

        self.income = float(input("Please enter your post-tax monthly income($):"))

    def update_savings(self):

        """Prompts user how much they would like to save per month"""
        self.savings = float(
            input("Please enter the amount you would like to save each month($):")
        )

    def calculate_budget(self):
        """Calculates user's budget"""
        self.budget = self.income - self.savings
        print("Your budget is:", str(self.budget), end="\n")

    def purchase_prompt(self):
        """Prompts user for a numerical value when adding their expense"""

        is_valid = False
        while is_valid == False:
            try:
                self.new_expense = float(input("Please enter your expense($):"))

                if self.new_expense == int or float:
                    is_valid = True

            except Exception as e:
                print("Wrong input!")

        return self.new_expense

    def purchase_date(self):
        """Asks the user the date of purchase for the expense"""

        # Enter date
        while True:
            self.date = input("Enter the date of purchase (MM-DD-YYYY):")
            if len(self.date) == 10 and re.match("^[0-9-]*$", self.date):
                break
            else:
                print("Please enter a valid date")
        return self.date

    def purchase_description(self):
        """Asks for a description of the purchase"""

        # Enter description
        self.description = input("Enter the description of purchase:")

        return self.description

    def purchase_category(self):
        """Asks what category the user would like to put their expense in"""

        # Given a choice of what to categorize the purchase
        print("Enter the category of purchase:")
        print("1. Groceries")
        print("2. Housing")
        print("3. Transportation/Car Maintenance")
        print("4. Travel")
        print("5. Eating out")
        print("6. Bills")
        print("7. Childcare")
        print("8. Pet Food and Care")
        print("9. Clothing and Personal Upkeep")
        print("10. Subscriptions")
        print("11. Entertainment")
        print("12. Loans")
        print("13. Large Purchases")
        print("14. Personal")
        print("15. Miscellaneous")

        dict = {
            1: "Groceries",
            2: "Housing",
            3: "Transportation/Car Maintenance",
            4: "Travel",
            5: "Eating Out",
            6: "Bills",
            7: "Childcare",
            8: "Pet Food and Care",
            9: "Clothing and Personal Upkeep",
            10: "Subscriptions",
            11: "Entertainment",
            12: "Loans",
            13: "Large Purchases",
            14: "Personal",
            15: "Miscellaneous",
        }

        while True:
            category_number = int(input())
            self.category = dict.get(category_number, "Please enter a valid number")
            break

        return self.category

    def purchase_method(self):
        """Asks how the user purchased their expense"""

        # Given a choice of what to categorize the method of payment
        print("Enter the method of purchase:")
        print("1. Credit Card")
        print("2. Debit Card")
        print("3. Cash")
        print("4. Paypal")
        print("5. Apple Pay")
        print("6. Venmo")

        while True:
            # Categorizes the method of payment based on user input
            method2 = int(input())
            if method2 == 1:
                self.method = "Credit Card"
                break
            if method2 == 2:
                self.method = "Debit Card"
                break
            if method2 == 3:
                self.method = "Cash"
                break
            if method2 == 4:
                self.method = "Paypal"
                break
            if method2 == 5:
                self.method = "Apple Pay"
                break
            if method2 == 6:
                self.method = "Venmo"
                break
            else:
                print("Please enter a valid number")

        return self.method

    def insert_to_database(self, date, description, category, new_expense, method):
        """Inputs all the data into the Expenses db"""

        # Inserting all the user input into the expense table
        # First set of parenthesis lists the columns, the next asks for the placeholders, then after, it passes the values obtained from the user
        sql = """INSERT INTO expense (Date, Description, Category, Price, MethodofPayment) VALUES ('{}','{}','{}','{}','{}');""".format(
            date, description, category, new_expense, method
        )

        self.cursor.execute(sql)
        self.connection.commit()

        print("Your expense has been recorded")

    def add_expense(self, new_expense):
        """Calculates the new budget"""
        self.budget = self.budget - new_expense

        return self.budget

    def show_budget(self):
        """Shows the user their current budget"""

        print("Your budget is ($):", str(self.budget), end="\n")

    def Add_Budget(self, budget):
        """Adds the budget"""

        self.budget = budget

    def add_to_current_budget(self):
        """Adds to the users current budget"""
        print("How much would you like to add to your current budget?")
        self.budget += int(input())

        print("Your current budget is ($):", str(self.budget), end="\n")

    def delete_expense(self, id):
        """Deletes an expense by id"""

        try:
            # Obtains the id from the user that they want to delete and deletes the row where that id is
            delete_id = """DELETE from expense where id = ?"""
            self.cursor.execute(delete_id, (id,))
            self.connection.commit()
            print("Expense deleted successfully")

        except sqlite3.Error as error:
            print("Failed to delete reocord from expense table", error)

    def delete_all_expenses(self):
        """Deletes all data from the expense db"""
        self.cursor.execute("DELETE FROM expense")

        self.connection.commit()

        print("Your table has been deleted")

    def view_all_expenses(self):
        """Let's the user view all of their expenses"""
        # This part is fetching all the data from the expense database
        self.cursor.execute("SELECT * FROM expense")
        expenses = self.cursor.fetchall()
        for expense in expenses:
            print(expense)

    def view_by_date(self, month, year):
        """Lets the user view their expenses depending on the date."""
        self.cursor.execute("SELECT * FROM expense")
        expenses = self.cursor.fetchall()

        # dictionary to keep track of total expenses for each category
        category_totals = {}

        for expense in expenses:
            expense_date = datetime.datetime.strptime(
                expense[1], "%m-%d-%Y"
            )  # convert string to date object
            if expense_date.month == int(month) and expense_date.year == int(year):
                category = expense[3]
                price = expense[4]
                if category in category_totals:
                    category_totals[category] += price
                else:
                    category_totals[category] = price

        for category, total in category_totals.items():
            print(f"Category: {category}, Total: {total}")

    def view_by_category(self, category):
        """Lets the user view their total expenses for a specific category."""
        self.cursor.execute("SELECT * FROM expense WHERE category = ?", (category,))
        expenses = self.cursor.fetchall()

        # calculate total expense for the given category
        total = 0
        for expense in expenses:
            total += expense[4]

        print(f"Total expenses for category {category}: {total}")


# Main Program
if __name__ == "__main__":

    E = Expense()

    # Setting up the money sign
    with open("money.txt", "r") as f:
        for line in f:
            print(line.rstrip())
    f.close()

    print("Welcome to your expense tracker!")

    # Asking for users income and how much they would like to save, which calculates their budget
    E.update_income()
    E.update_savings()
    E.calculate_budget()

    # While loop that goes back to the main options the user has
    while True:
        # Shows user options
        E.display_menu()

        choice = int(input())

        # Adding Expense
        if choice == 1:
            new_expense = E.purchase_prompt()

            print("Your new budget is ($):", E.add_expense(new_expense), end="\n")

            date = E.purchase_date()
            description = E.purchase_description()
            category = E.purchase_category()
            method = E.purchase_method()

            E.insert_to_database(date, description, category, new_expense, method)

        elif choice == 2:
            # Letting the user view their expenses
            print("Please select what you would like to do:")
            print("1. Delete expense")
            print("2. Delete all expenses")

            delete_choice = int(input())

            # Deletes row of expense
            if delete_choice == 1:
                print("Please type which row you'd like to delete (based on the id):")
                delete_id = int(input())
                E.delete_expense(delete_id)

            # Deletes table of expenses: Resets table, but you need to restart program and enter your budget
            elif choice == 2:
                E.delete_all_expenses()

        elif choice == 3:
            # Let's the user see their expenses
            print("Please select what you would like to do:")
            print("1. View expenses by category")
            print("2. View expenses by date")
            print("3. View all expenses")

            view_choice = int(input())

            if view_choice == 1:
                print("Which category would you like to view?")
                view_category = input()
                E.view_by_category(view_category)

            elif view_choice == 2:
                print("Which month would you like to view? (Enter as MM)")
                month = int(input())
                print("Which year would you like to view? (Enter as YYYY)")
                year = int(input())

                E.view_by_date(month, year)
            else:
                E.view_all_expenses()

        # Shows the user their current budget
        elif choice == 4:
            E.show_budget()
        else:
            print("Please enter a valid number")
