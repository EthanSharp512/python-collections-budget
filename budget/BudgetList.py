from . import Expense

expenses = Expense.Expenses()
expenses.read_expenses("data/spending_data.csv")

class BudgetList():
    def __init__(self, budget):
        self.budget = budget
        self.sum_expenses = 0 
        self.expenses = []
        self.sum_overages = 0
        self.overages = []

    def __append__(self, item):
        if((self.sum_expenses + item) < self.budget):
            self.expenses.append(item)
            self.sum_expenses += item
        else:
            self.overages.append(item)
            self.sum_overages += item

    def __len__(self):
        return (self.expenses.length() + self.overages.length())

def main():
    myBudgetList = BudgetList(1200)

    for expense in expenses.list:
        myBudgetList.append(expense.amount)

    myBudgetListLen = str(myBudgetList.len())
    print(f"The count of all expenses: {myBudgetListLen}")

if __name__ == "__main__":
    main()