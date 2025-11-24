import os
import csv
from datetime import datetime

FILE_NAME = "expenses.csv"
FIELDS = ["Date", "Category", "Amount", "Description"]

# Create the file if it doesn't exist
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(FIELDS)
        print(" expenses.csv created successfully!\n")


def add_expense():
    print("\n Add New Expense")
    category = input("Enter category (Food/Travels/Bills/Others): ").title()
    amount = input("Enter your amount: ")
    description = input("Enter a short note: ")

    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    
    print(" Expense added successfully!\n")


def view_expenses():
    print("\n Expense History ")
    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(" | ".join(row))
    except:
        print("No data was found.please add expenses first.\n")


def total_spent():
    print("\n Total Spending ")
    total = 0
    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # skip header

            for row in reader:
                total += float(row[2])
        
        print(f" Total money spent so far: Rs. {total}\n")
    except:
        print(" No data found.\n")


def filter_by_category():
    print("\n--- Filter by Category ---")
    category = input("Enter category to filter: ").title()

    total = 0
    print(f"\n Showing all expenses under: {category}\n")

    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.reader(file)
            next(reader)

            found = False
            for row in reader:
                if row[1] == category:
                    print(" | ".join(row))
                    total += float(row[2])
                    found = True
            
            if not found:
                print(" No expenses found in this category.")
            else:
                print(f"\n Total spent in {category}: Rs. {total}\n")

    except:
        print(" Error occured while reading this file.\n")


def menu():
    initialize_file()

    while True:

        print("     EXPENSE TRACKER")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Total Money Spent")
        print("4. Filter by Category")
        print("5. Exit")

        choice = input("\nEnter choice (1-5): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_spent()
        elif choice == "4":
            filter_by_category()
        elif choice == "5":
            print("\n Exiting... saayonara!")
            break
        else:
            print(" this is an invalid choice, try again.\n")


# Run the program
if __name__ == "__main__":
    menu()
