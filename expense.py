import uuid
import time
import datetime as dt
from typing import Optional

class Expense:

    def __init__(self, title: str, amount: float) -> None:

        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.created_at = f"{dt.datetime.now(dt.UTC): %Y-%m-%d %H:%M:%S}" 
        self.updated_at = None

    def update(self, title: Optional[str] = None, amount: Optional[float] = None) -> None:

        if title:
            self.title = title
        
        if amount:
            self.amount = amount

        self.updated_at = f"{dt.datetime.now(dt.UTC):%Y-%m-%d %H:%M:%S}"

    def to_dict(self) -> dict[str, str|float]:

        return self.__dict__
    


class ExpenseDB:

    def __init__(self) -> None:

        self.expenses: list[Expense] = []


    def add_expense(self, expense: Expense) -> None:
       
        self.expenses.append(expense)

    def remove_expense(self, expense: Expense) -> None:

        self.expenses.remove(expense)


    def get_expense_by_id(self, id: str) -> Expense:

        return [expense for expense in self.expenses if expense.id == id][0]
    
    
    def get_expense_by_title(self, title: str) -> Expense:

        return [expense for expense in self.expenses if expense.title == title][0]
    
    
    def to_dict(self) -> list[dict[str, str|float]]:

        return [expense.to_dict() for expense in self.expenses]
    

def main() -> None:

    my_expense = Expense("Food Expense", 200.0)
    print(my_expense.to_dict())

    time.sleep(1)

    my_expense.update(amount=250.0)
    print(my_expense.to_dict())

    my_expense2 = Expense("Car", 20000.00)

    expense_database = ExpenseDB()
    expense_database.add_expense(my_expense)
    expense_database.add_expense(my_expense2)
    print(expense_database.to_dict())

    my_expense2.update(title="truck")

    print(expense_database.to_dict())

    expense_database.remove_expense(my_expense2)
    print(expense_database.to_dict())

    my_expense3 = Expense("House", 200000.00)
    expense_database.add_expense(my_expense3)
    print(expense_database.to_dict())

    expense_3 = expense_database.get_expense_by_id(my_expense3.id)
    print(expense_3.to_dict())

    food_expense = expense_database.get_expense_by_title("Food Expense")
    print(food_expense.to_dict())	



if __name__ == "__main__":
    main()

    