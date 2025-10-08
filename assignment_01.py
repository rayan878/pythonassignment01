# Student Name: Rayan Lamba
# Date: October 08, 2025
# Assignment: Building a Simple Expense Tracker App

print("Welcome to the Simple Expense Tracker App! This tool helps you record and summarize your daily expenses.")

categories = []
amounts = []

while True:
    category = input("Enter expense category: ")
    amount = float(input("Enter amount: "))
    categories.append(category)
    amounts.append(amount)
    
    more = input("Do you want to add more? (yes/no): ").strip().lower()
    if more != 'yes':
        break

if amounts:
    total = sum(amounts)
    average = total / len(amounts)
else:
    total = 0
    average = 0

print("\nYour Expenses:")
for cat, amt in zip(categories, amounts):
    print(f"{cat} - {amt}")

print(f"Total Expense: {total}")
print(f"Average Expense: {average}")
