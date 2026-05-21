from models.transaction import Expense, Income

class FinanceService:
    def __init__(self):
        self._transactions = []  
    def load_from_data(self, data_list):
        self._transactions = []
        for item in data_list:
            try:
                if item["type"] == "expense":
                    t = Expense(
                        amount=item["amount"],
                        date=item["date"],
                        category=item.get("category", "other"),
                        description=item.get("description", "")
                    )
                else:
                    t = Income(
                        amount=item["amount"],
                        date=item["date"],
                        description=item.get("description", "")
                    )
                self._transactions.append(t)
            except KeyError as e:
                print(f"Skipping invalid entry (missing field: {e})")

    def add_expense(self, amount, date, category, description=""):
        expense = Expense(amount, date, category, description)
        self._transactions.append(expense)
        return expense

    def add_income(self, amount, date, description=""):
        income = Income(amount, date, description)
        self._transactions.append(income)
        return income

    def delete_last_transaction(self):
        if self._transactions:
            removed = self._transactions.pop()
            print(f"Removed: {removed}")
        else:
            print("No transactions to remove.")

    def get_all_transactions(self):
        return self._transactions

    def get_balance(self):
        balance = 0
        for t in self._transactions:
            if t.get_type() == "income":
                balance += t.get_amount()
            else:
                balance -= t.get_amount()
        return balance

    def get_transactions_by_month(self, year, month):
        month_prefix = f"{year}-{month:02d}"
        return list(filter(lambda t: t.get_date().startswith(month_prefix), self._transactions))

    def expense_generator(self):
        for t in self._transactions:
            if t.get_type() == "expense":
                yield t

    def get_category_totals(self):  
        totals = {}
        for t in self.expense_generator():
            cat = t.get_category()
            totals[cat] = totals.get(cat, 0) + t.get_amount()
        return totals
    
    def detect_overspending(self, budgets): 
        category_totals = self.get_category_totals()
        warnings = []
        for category, limit in budgets.items():
            spent = category_totals.get(category, 0)
            if spent > limit:
                warnings.append((category, spent, limit))
        return warnings
    
    def get_unique_categories(self):
        return set(t.get_category() for t in self.expense_generator())
    
    def get_all_dates(self):
        dates = set()
        for t in self._transactions:
            parts = t.get_date().split("-")
            dates.add(tuple(parts))
        return sorted(dates)
    
    def to_dict_list(self):
        return [t.to_dict() for t in self._transactions]
