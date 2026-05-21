class Transaction:

    def __init__(self, transaction_type, amount, date, category=None, description=""):
        self._type = transaction_type
        self._amount = amount
        self._date = date
        self._category = category
        self._description = description

    def get_type(self):
        return self._type

    def get_amount(self):
        return self._amount

    def get_date(self):
        return self._date

    def get_category(self):
        return self._category

    def get_description(self):
        return self._description

    def to_dict(self):
        return {
            "type": self._type,
            "amount": self._amount,
            "date": self._date,
            "category": self._category,
            "description": self._description
        }

    def __str__(self):
        return f"[{self._date}] {self._type.upper()} | ${self._amount:.2f} | {self._category}"
