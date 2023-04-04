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
        # Lets the user their expenses in a pie chart, line graph, or by category
        print("3. View Expenses")
        # Lets the user see their current budget left
        print("4. Current budget")

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

                if self.new_expense == int:
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

        while True:
            descrip = int(input())
            if descrip == 1:
                self.category = "Groceries"
                break
            if descrip == 2:
                self.category = "Housing"
                break
            if descrip == 3:
                self.category = "Transportation/Car Maintenance"
                break
            if descrip == 4:
                self.category = "Travel"
                break
            if descrip == 5:
                self.category = "Eating out"
                break
            if descrip == 6:
                self.category = "Bills"
                break
            if descrip == 7:
                self.category = "Childcare"
                break
            if descrip == 8:
                self.category = "Pet Food and Care"
                break
            if descrip == 9:
                self.category = "Clothing and Personal Upkeep"
                break
            if descrip == 10:
                self.category = "Subscriptions"
                break
            if descrip == 11:
                self.category = "Entertainment"
                break
            if descrip == 12:
                self.category = "Loans"
                break
            if descrip == 13:
                self.category = "Large Purchases"
                break
            if descrip == 14:
                self.category = "Personal"
                break
            if descrip == 15:
                self.category = "Miscellaneous"
                break
            else:
                print("Please enter a valid number")

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


# Main Program
if __name__ == "__main__":

    E = Expense()

    # Setting up the money sign; this is just for fun
    with open("money.txt", "r") as f:
        for line in f:
            print(line.rstrip())

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
            pass
        elif choice == 3:
            pass
        # Shows the user their current budget
        elif choice == 4:
            E.show_budget()
        else:
            print("Please enter a valid number")