import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import unittest
from models.transaction import Expense, Income
from services.finance_service import FinanceService
from utils.validator import validate_amount, validate_date, validate_category


class TestTransactionModels(unittest.TestCase):
    def test_expense_creation(self):
        exp = Expense(50.0, "2026-05-01", "food", "Lunch")
        self.assertEqual(exp.get_type(), "expense")
        self.assertEqual(exp.get_amount(), 50.0)
        self.assertEqual(exp.get_category(), "food")

    def test_income_creation(self):
        """Income object should store values correctly."""
        inc = Income(1000.0, "2026-05-01", "Salary")
        self.assertEqual(inc.get_type(), "income")
        self.assertEqual(inc.get_amount(), 1000.0)

    def test_expense_is_large(self):
        small = Expense(50.0, "2026-05-01", "food")
        big = Expense(500.0, "2026-05-01", "shopping")
        self.assertFalse(small.is_large(200))
        self.assertTrue(big.is_large(200))

    def test_to_dict(self):
        exp = Expense(30.0, "2026-05-01", "transport")
        result = exp.to_dict()
        self.assertIsInstance(result, dict)
        self.assertEqual(result["type"], "expense")
        self.assertEqual(result["amount"], 30.0)


class TestFinanceService(unittest.TestCase):
    def setUp(self):
        self.fs = FinanceService()
        self.fs.add_income(1000.0, "2026-05-01", "Salary")
        self.fs.add_expense(100.0, "2026-05-02", "food")
        self.fs.add_expense(200.0, "2026-05-03", "transport")

    def test_get_balance(self):
        balance = self.fs.get_balance()
        self.assertAlmostEqual(balance, 700.0)

    def test_add_transaction_count(self):
        all_t = self.fs.get_all_transactions()
        self.assertEqual(len(all_t), 3)

    def test_category_totals(self):
        totals = self.fs.get_category_totals()
        self.assertEqual(totals.get("food"), 100.0)
        self.assertEqual(totals.get("transport"), 200.0)

    def test_filter_by_month(self):
        may_transactions = self.fs.get_transactions_by_month(2026, 5)
        self.assertEqual(len(may_transactions), 3)

    def test_overspending_detected(self):
        budgets = {"transport": 100}
        warnings = self.fs.detect_overspending(budgets)
        self.assertEqual(len(warnings), 1)
        self.assertEqual(warnings[0][0], "transport")

    def test_no_overspending(self):
        budgets = {"food": 500, "transport": 500}
        warnings = self.fs.detect_overspending(budgets)
        self.assertEqual(len(warnings), 0)

    def test_delete_last_transaction(self):
        self.fs.delete_last_transaction()
        self.assertEqual(len(self.fs.get_all_transactions()), 2)

    def test_empty_balance(self):
        fs = FinanceService()
        self.assertEqual(fs.get_balance(), 0)


class TestValidators(unittest.TestCase):

    def test_valid_amount(self):
        self.assertEqual(validate_amount("99.5"), 99.5)

    def test_invalid_amount_negative(self):
        with self.assertRaises(ValueError):
            validate_amount("-10")

    def test_invalid_amount_text(self):
        with self.assertRaises(ValueError):
            validate_amount("abc")

    def test_valid_date(self):
        self.assertEqual(validate_date("2026-05-01"), "2026-05-01")

    def test_invalid_date_format(self):
        with self.assertRaises(ValueError):
            validate_date("01-05-2026")

    def test_valid_category(self):
        self.assertEqual(validate_category("food"), "food")

    def test_invalid_category(self):
        with self.assertRaises(ValueError):
            validate_category("vacation")

    def test_category_case_insensitive(self):
        self.assertEqual(validate_category("Food"), "food")


if __name__ == "__main__":
    unittest.main()
