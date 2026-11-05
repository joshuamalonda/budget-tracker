# Asking the user for their monthly budget as an integer
monthly_budget = int(input("What is your monthly budget "))

# 5 categories stored in a dictionary alongside the total expense amount for each category as the value
categories = {
    "Transport": 0,
    "Food": 0,
    "Leisure": 0,
    "Housing": 0,
    "Subscriptions": 0
}

# Created a list where all the transactions will be kept
transactions = []

# Asking the user to input an expense amount as an integer
expense = int(input("Please enter an expense amount "))

# Asking the user to type one category and python will remove the spaces in their answers and will also put all the letters in lowercase and capitalize the first letter in the word
category = input(
    "Please select one category: Transport, Food, Leisure, Housing, Subscriptions ").strip().lower().capitalize()

# Now we are adding the category and expense the user typed into the transactions list we created, and we are storing as a dictionary within a list
transactions.append(
    {
        "Category": category,
        "Expense": expense
    }
)

# Here we are adding the expense the user typed to the right category (key) within the categories dictionary
categories[category] = categories[category] + expense

# Now we are asking the user if they would like to add another expense and the user will need to type yes or no
add_expenses = input("Would you like to add another expense yes/no ").strip().lower()

# Created a while loop so if the user say yes it will ask for their expense amount go through the process and will ask if they would like to add another expense and will keep on going until the user says no
while add_expenses == "yes":
    expense = int(input("Please enter an expense amount "))
    category = input(
        "Please select one category: Transport, Food, Leisure, Housing, Subscriptions ").strip().lower().capitalize()
    transactions.append(
        {
            "Category": category,
            "Expense": expense
        }
    )
    categories[category] = categories[category] + expense
    add_expenses = input("Would you like to add another expense yes/no ").strip().lower()

# If the user types no then the program thanks them for adding all of their expenses
if add_expenses == "no":
    print("Thanks for adding all of your expenses ")

# This calculates the total amount of money spent by the user 
total_expenses = sum(categories.values())

# This calculates the average expense by doing the total amount spent divided by the amount of individual transactions
average_expense = total_expenses / len(transactions)

# Then rounding it to the second decimal point
average_expense = round(average_expense, 2)

# This is what we will print at the end once the user says no
print(f""" 
     Budget Tracker

     Monthly Budget : £{monthly_budget}

     Total Spent : £{total_expenses}
     
     Average Expense : £{average_expense}

"""
      )

# Variable that has the highest category total
biggest_amount = max(categories.values())

# For loop that that prints the biggest key value pair by first seeing if the value is the highest category total
print("Biggest Category: ")
for key, value in categories.items():
    if value == biggest_amount:
        print(f"{key} (£{value})")

# Another for loop that prints key and value pairs within the categories dictionary only if the expense is more than 0
print("Spending by category total: ")
for key, value in categories.items():
    if value > 0:
        print(f"{key}: £{value}")

# Calculating the money left
money_left = monthly_budget - total_expenses

# Conditional statement so the user knows if they're under or over budget or if they've spent all their money
if monthly_budget > total_expenses:
    print(f"You have £{money_left} left")
elif monthly_budget == total_expenses:
    print(f"You have used up all of your budget")
else:
    over_budget = money_left * -1
    print(f"You are over budget by £{over_budget}")

# This for loop basically prints all of the transactions within the transactions list we created earlier
print("Transactions: ")
for i in transactions:
    print(f"{i['Category']}: £{i['Expense']}")
