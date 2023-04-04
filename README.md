# expense_tracker

Simple program to keep of your expenses.

# Project Description
This program is designed to have you input each expense you have. When you input the expense, the programs asks for details such as the date the purchase was made, the amount, a description of the expense, the category you think it belongs in, and the method of payment. The program also allows you to see visually where you are spending your money. That could be in the form of a pie graph, line graph, or in the terminal window itself. The program also lets you know how much of your budget is left.

# How to run the project
Simply download all the files in the src and test folder and the money.txt file.

Once everything is downloaded,

1. Run the expense_tracker file which is the main program and where you'll be inputting all of your expenses.
The image below is what you should see when you run your code: 
Capture.PNG

expense_tracker: This is the main window, where you'll be inputting all of your expenses.

expenses_database: This creates your database that stores all of your expenses.

test_current_budget: This is a unittest file that makes sure your budget is correctly calculating. Make sure that when you are running the test, you are in the same directory as the test folder and the src folder.

Run the following in the terminal: python -m unittest .\test\test_current_budget

money.txt: This is the money sign that will pop up in the beginning of your code.

# How to use the project
The terminal window will prompt you for an input; simply follow the commands
