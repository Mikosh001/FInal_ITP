import json
import os


def load_transactions(filepath):
    if not os.path.exists(filepath):
        print(f"File '{filepath}' not found, starting fresh.")
        return []

    with open(filepath, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            print("File is corrupted or contains invalid JSON.")
            return []
        except Exception as e:
            print(f"Something went wrong while loading: {e}")
            return []


def save_transactions(filepath, transactions_list):
    try:
        with open(filepath, "w") as f:
            json.dump(transactions_list, f, indent=4)
    except Exception as e:
        print(f"Failed to save data: {e}")
    else:
        print("Saved.")
