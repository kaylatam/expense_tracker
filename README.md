# expense_tracker

Simple program to keep of your expenses.

![Capture](https://user-images.githubusercontent.com/65250638/229909617-a42ee551-589a-4a4e-9de4-274891833eff.PNG)

# Project Description
This program is designed to have you input each expense you have. When you input the expense, the programs asks for details such as the date the purchase was made, the amount, a description of the expense, the category you think it belongs in, and the method of payment. The program also allows you to see visually where you are spending your money. That could be in the form of a pie graph, line graph, or in the terminal window itself. The program also lets you know how much of your budget is left.

- **expense_tracker**: Main code

- **expenses_database**: This creates your database that stores all of your expenses.

- **test_current_budget**: This is a unittest file that makes sure your budget is correctly calculating. Make sure that when you are running the test, you are in the same directory as the test folder and the src folder.

- **money.txt**: This is the money sign that will pop up in the beginning of your code. MAKE SURE THAT THIS FILE WILL BE IN THE SAME FOLDER AS YOUR src AND test FOLDER

# How to run the project
Simply download all the files in the src and test folder and the money.txt file. With the expense.db file in the src folder, delete it once it is downloaded. You will create your own with the expenses_database file. With the money.txt file and your expenses.db file, make sure that it's in the same pathway as the program you are using to run your code. 

Once everything is downloaded,

1. Run the expenses_database program; this will create your database and where all of your expenses will be inputted

2. Run the expense_tracker file which is the main program and where you'll be inputting all of your expenses.
 

3. Follow the prompts that come up in the terminal. 


To run test_current_budget:

1. Run the following in the terminal: python -m unittest .\test\test_current_budget


# How to use the project
The terminal window will ask you for your budget, how much you'd like to save, and from there, you just input your expenses. You'll have the option to also view your current budget, add to your current budget, delete expenses, etc. 
