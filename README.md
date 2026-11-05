Budget Tracker

A command line budget tracker written in Python. Enter your monthly budget and your expenses, and it shows where your money went and how much you have left.

What it does

Asks for your monthly budget
Lets you add as many expenses as you like, each with a category: Transport, Food, Leisure, Housing or Subscriptions
Keeps a running total for each category
Stores every individual transaction
Prints a summary with:
total spent and average expense
your biggest spending category
spending by category (only categories you've spent in)
how much budget is left, or how far over budget you are
your full transaction history

How to run it

You need Python 3. No extra libraries are required.

What is your monthly budget 2000
Please enter an expense amount 175
Please select one category: Transport, Food, Leisure, Housing, Subscriptions Housing
Would you like to add another expense yes/no yes
Please enter an expense amount 20
Please select one category: Transport, Food, Leisure, Housing, Subscriptions Food
Would you like to add another expense yes/no yes
Please enter an expense amount 100
Please select one category: Transport, Food, Leisure, Housing, Subscriptions Leisure
Would you like to add another expense yes/no no
Thanks for adding all of your expenses 
 
     Budget Tracker

     Monthly Budget : £2000

     Total Spent : £295
     
     Average Expense : £98.33


Biggest Category: 
: Housing (£175)
Spending by category total: 
Food: £20
Leisure: £100
Housing: £175
You have £1705 left
Transactions: 
Housing: £175
Food: £20
Leisure: £100


How it works

The program keeps two separate records of your spending:

Category totals: a dictionary that maps each category to the total spent in it. Each new expense is added to the right category's running total.
Transaction history: a list of dictionaries, with one dictionary per expense holding its category and amount.

The totals make the summary quick to calculate, and the history keeps the detail of every individual expense. Both are updated every time an expense is added.

What I learned

When to use a dictionary and when to use a list, and how to store dictionaries inside a list
Updating a running total by reading the old value, adding to it and storing it back
Using a while loop to keep asking for input until the user is finished
Looping through dictionaries with .items() and filtering with if
Using built-in functions (sum(), len(), max() and round()) to replace longer code
Debugging code 

Known limitations

Entering a category that isn't on the list crashes the program.
Entering text instead of a number for the budget or an expense crashes the program.
Amounts must be whole pounds.
Data isn't saved, so everything is lost when the program closes.