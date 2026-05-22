import os
from services.finance_service import FinanceService
from services.report_service import ReportService
from utils.file_handler import load_transactions, save_transactions
from utils.validator import validate_amount, validate_date, validate_category, VALID_CATEGORIES

DATA_FILE = os.path.join("data", "transactions.json")

BUDGETS = {
    "food": 300,
    "transport": 100,
    "entertainment": 150,
    "shopping": 250,
    "bills": 200,
    "health": 200,
    "other": 100
}


def print_menu():
    print("\n========= Personal Finance Tracker =========")
    print("  1. Add Income")
    print("  2. Add Expense")
    print("  3. View All Transactions")
    print("  4. View Balance")
    print("  5. View Category Breakdown")
    print("  6. View Monthly Summary")
    print("  7. View Statistics")
    print("  8. Check Overspending")
    print("  9. View Large Expenses")
    print(" 10. Delete Last Transaction")
    print("  0. Save and Exit")
    print("============================================")


def get_input(prompt, validator=None):
    while True:
        value = input(prompt).strip()
        if validator is None:
            return value
        try:
            return validator(value)
        except ValueError as e:
            print(f"  Input error: {e}")


def handle_add_income(fs):
    print("\n-- Add Income --")
    amount = get_input("  Amount: $", validate_amount)
    date = get_input("  Date (YYYY-MM-DD): ", validate_date)
    description = input("  Description (optional): ").strip()
    t = fs.add_income(amount, date, description)
    print(f"  Added: {t}")


def handle_add_expense(fs):
    print("\n-- Add Expense --")
    print(f"  Categories: {', '.join(sorted(VALID_CATEGORIES))}")
    amount = get_input("  Amount: $", validate_amount)
    date = get_input("  Date (YYYY-MM-DD): ", validate_date)
    category = get_input("  Category: ", validate_category)
    description = input("  Description (optional): ").strip()
    t = fs.add_expense(amount, date, category, description)
    print(f"  Added: {t}")


def handle_monthly_summary(report):
    print("\n-- Monthly Summary --")
    try:
        year = int(input("  Year (e.g. 2026): ").strip())
        month = int(input("  Month (1-12): ").strip())
        if not (1 <= month <= 12):
            print("  Invalid month.")
            return
        report.print_monthly_summary(year, month)
    except ValueError:
        print("  Please enter valid numbers for year and month.")

def main():
    data = load_transactions(DATA_FILE)

    fs = FinanceService()
    fs.load_from_data(data)

    report = ReportService(fs)

    print("Welcome to Personal Finance Tracker!")
    print(f"Loaded {len(fs.get_all_transactions())} transactions from file.")

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            handle_add_income(fs)
        elif choice == "2":
            handle_add_expense(fs)
        elif choice == "3":
            report.print_all_transactions()
        elif choice == "4":
            report.print_balance()
        elif choice == "5":
            report.print_category_breakdown()
        elif choice == "6":
            handle_monthly_summary(report)
        elif choice == "7":
            report.print_statistics()
        elif choice == "8":
            report.print_overspending_warnings(BUDGETS)
        elif choice == "9":
            try:
                threshold = int(float(input("  Show expenses over: $").strip()))
            except ValueError:
                threshold = 200
            report.print_large_expenses(threshold)
        elif choice == "10":
            fs.delete_last_transaction()
        elif choice == "0":
            save_transactions(DATA_FILE, fs.to_dict_list())
            print("Goodbye!")
            break
        else:
            print("  Invalid option. Please choose a number from the menu.")


if __name__ == "__main__":
    main()


