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
