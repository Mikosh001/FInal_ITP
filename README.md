Personal Finance Tracker
A Python application to track personal income and expenses, generate reports, and detect overspending.

Course: Introduction to Programming 2 (Python) — Final Project  
Case: Case 3 — Personal Finance Tracker

Team Members:
Name                 - Contribution
Mirzatayev Bagdaulet - models/, transaction classes
Berdibek Meirbek     - services/finance_service.py, report_service.py
Altair Abdraisov     - tests/test_finance.py, main.py 
Daryn Yerbol         - utils/file_handler.py, validator.py


Features:

 Add income and expense transactions
 View full transaction history
 View current balance
 Category-based expense breakdown
 Monthly income/expense summary
 Overspending detection based on custom budgets
 Large expense filtering
 Save and load data from JSON file


## Project Structure

```
finance_tUracker/
├── main.py                    # Entry point, CLI menu
├── models/
│   └── transaction.py         # Transaction, Expense, Income classes
├── services/
│   ├── finance_service.py     # Core business logic
│   └── report_service.py      # Report printing
├── utils/
│   ├── file_handler.py        # JSON read/write
│   └── validator.py           # Input validation (regex, type checks)
├── tests/
│   └── test_finance.py        # nit tests
├── data/
│   └── transactions.json      # Sample data file
└── README.md


```json
[
    {"type": "expense", "category": "food", "amount": 20, "date": "2026-05-01", "description": "Lunch"},
    {"type": "income", "amount": 1000, "date": "2026-05-01", "description": "Salary"}
]
