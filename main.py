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



