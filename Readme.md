Personal Expense Tracker

This project is nothing but a simple command-line Expense Tracker built with Python. It helps us record and track their daily spending in a cool and proper systematic way.

The data gets stored in a fresh .csv file, making the system light and easy to move around.

Features

- Creates a CSV file automatically if it isn”t there.
- Adds new expenses (cateogory, amount, date, notes)
- Shows all expense entries
- Shows total money spent
- Filters expenses by category
- Exits cleanly

How does it work

When the program runs, it shows a menu with options. Users can choose an action, like adding or viewing expenses, by entering a number of any choice.

The program saves and retrieves data from expenses.csv using Python's CSV module.

-----------------   Technologies Used  -------------------
Component                                                      Purpose  
Python                                                                 Main programming language  
CSV Module                                                      File storage and reading  
OS Module                                                         File handling (checking if CSV exists)  
  datetime                                                               Auto-saving expense date  

CSV File Structure

The tracker saves data in this format:
EXAMPLE
 

Date, Category, Amount, Description
--------   How to Run

~ Install Python (if it’s not installed).

~ Save the script as:

 expense_tracker.py

~ Run the file in the terminal or VS Code:

python expense_tracker.py

Menu Options Preview  
     EXPENSE TRACKER  
1. Add Expense  
2. View All Expenses  
3. Total Money Spent  
4. Filter by Category  
5. Exit  

Example Output  

 

In future I aim to Improve it by adding these things such as :

- Adding graphical charts  
- Export PDF summary  
- Monthly spending report  
- User login system  
- GUI using Tkinter or Web Interface  

License

This project is made for project purpose. Feek free to use it as you like.

