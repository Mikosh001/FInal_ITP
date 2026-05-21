# utils/validator.py
# validation for amount, date, and category inputs

import re

VALID_CATEGORIES = {"food", "transport", "entertainment", "health", "bills", "shopping", "other"}


def validate_amount(amount_str):
    try:
        value = float(amount_str)
    except ValueError:
        raise ValueError(f"'{amount_str}' doesn't look like a number.")

    if value <= 0:
        raise ValueError("Amount has to be greater than zero.")

    return value


def validate_date(date_str):
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_str):
        raise ValueError(f"'{date_str}' — expected format is YYYY-MM-DD.")
    return date_str


def validate_category(category_str):
    category = category_str.strip().lower()
    if category not in VALID_CATEGORIES:
        allowed = ", ".join(sorted(VALID_CATEGORIES))
        raise ValueError(f"'{category}' is not a valid category. Pick one of: {allowed}")
    return category