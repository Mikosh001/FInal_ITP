class ReportService:

    def __init__(self, finance_service):
        self._fs = finance_service
    def print_balance(self):
        balance = self._fs.get_balance()
        print("\n==============================")
        if balance >= 0:
            print(f"Current Balance: ${balance:.2f}")
        else:
            print(f"Current Balance: -${abs(balance):.2f}")
        print("==============================")

    def print_all_transactions(self):
        transactions = self._fs.get_all_transactions()
        print("\n--- All Transactions ---")
        if len(transactions) == 0:
            print("No transactions found.")
            return
        count = 1
        for t in transactions:
            print(f"{count}. {t}")
            count += 1

    def print_category_breakdown(self):
        totals = self._fs.get_category_totals()
        print("\n--- Expenses by Category ---")
        if len(totals) == 0:
            print("No expenses yet.")
            return
        for category in totals:
            print(f"{category}: ${totals[category]:.2f}")
    
    def print_monthly_summary(self, year, month):
        transactions = self._fs.get_transactions_by_month(year, month)
        print(f"\n--- Monthly Summary ({year}-{month:02d}) ---")
        if len(transactions) == 0:
            print("No data for this month.")
            return
        income_total = 0
        expense_total = 0
        for t in transactions:
            if t.get_type() == "income":
                income_total += t.get_amount()
            else:
                expense_total += t.get_amount()
        print(f"Income : ${income_total:.2f}")
        print(f"Expense: ${expense_total:.2f}")
        print(f"Savings: ${income_total - expense_total:.2f}")

