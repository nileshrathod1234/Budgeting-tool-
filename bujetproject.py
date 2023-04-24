import os
import csv

# A class to represent a budget
class Budget:
  def __init__(self, budget_file):
    self.budget_file = budget_file
    self.expenses = []
    self.categories = {}
    self.load_budget()

  # Load the budget data from the CSV file
  def load_budget(self):
    if os.path.exists(self.budget_file):
      with open(self.budget_file, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip the header row
        for row in reader:
          if not row:
            continue
          category, amount, date = row
          self.add_expense(category, float(amount), date)

  # Add an expense to the budget
  def add_expense(self, category, amount, date): #'Food', 50.00, '2022-01-01'
    self.expenses.append({
      'category': category,
      'amount': amount,
      'date': date
    })
    if category in self.categories:
      self.categories[category] += amount
    else:
      self.categories[category] = amount


  # Get the total amount spent in a given category
  def get_category_total(self, category):
    if category in self.categories:
      return self.categories[category]
    else:
      return 0

  # Get the total amount spent
  def get_total(self):
    total = 0
    for expense in self.expenses:
      total += expense['amount']
    return total

  # Save the budget data to the CSV file
  def save(self):
    with open(self.budget_file, 'w') as f:
      writer = csv.writer(f)
      for expense in self.expenses:
        writer.writerow([expense['category'], expense['amount'], expense['date']])

# Create a budget object and add some expenses
budget = Budget('budget.csv')
budget.add_expense('Food', 50.00, '2022-01-01')
budget.add_expense('Clothing', 75.00, '2022-01-02')
budget.add_expense('Entertainment', 25.00, '2022-01-03')
budget.add_expense('Food',200.00,'2023-01-10')
budget.add_expense('Clothing',100,'04-01-2023')
# Print the total amount spent on Food
print(budget.get_category_total('Food'))  # Output: 250.0

# Print the total amount spent
print(budget.get_total())  # Output: 350.0

# Save the budget data to the CSV file
budget.save()

