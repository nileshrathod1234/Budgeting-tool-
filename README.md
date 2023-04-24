# Budgeting-tool in python
 This project aims to create a simple yet effective budgeting tool using Python that helps users to track and manage their expenses. The tool provides a way to add expenses, view the total amount spent in a given category, and view the overall total spent. Additionally, the tool allows users to save and load their budget data using CSV files.
The project consists of a single Python file that contains the Budget
class. The Budget class has the following methods:

__init__(self, budget_file): Initializes the Budget object with the
given budget file.
load_budget(self): Loads the budget data from the specified CSV file.
add_expense(self, category, amount, date): Adds an expense with the
given category, amount, and date to the budget.
get_category_total(self, category): Returns the total amount spent in
the given category.
get_total(self): Returns the total amount spent across all categories.
save(self): Saves the budget data to the specified CSV file.
