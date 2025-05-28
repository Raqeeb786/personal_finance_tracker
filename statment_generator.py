import random
import datetime
import json

# Helper function to generate random transactions
def generate_transactions(start_balance, num_transactions, start_date, end_date):
    descriptions = [
        "Paycheck", "ATM Withdrawal", "Online Shopping - Amazon", "Grocery Store",
        "Electricity Bill", "Water Bill", "Internet Bill", "Mobile Recharge",
        "Dining - Restaurant", "Fuel Station", "Gym Membership", "Movie Tickets",
        "Credit Card Payment", "Loan EMI", "Mutual Fund Investment", "NEFT Transfer",
        "IMPS Transfer", "UPI Payment", "Subscription - Netflix", "Cash Deposit"
    ]
    transactions = []
    balance = start_balance
    current_date = start_date

    for _ in range(num_transactions):
        amount = round(random.uniform(50, 5000), 2)
        transaction_type = random.choices(["credit", "debit"], weights=[0.4, 0.6])[0]

        if transaction_type == "credit":
            balance += amount
        else:
            if balance - amount >= 0:
                balance -= amount
            else:
                continue  # skip if not enough balance

        description = random.choice(descriptions)
        random_days = random.randint(1, 4)
        current_date += datetime.timedelta(days=random_days)
        if current_date > end_date:
            break

        transactions.append({
            "date": current_date.strftime("%Y-%m-%d"),
            "description": description,
            "type": transaction_type,
            "amount": amount,
            "balance": round(balance, 2)
        })

    return transactions

# Function to generate statement for a bank
def generate_bank_statement(bank_name):
    start_date = datetime.date(2024, 1, 1)
    end_date = datetime.date(2024, 3, 31)
    account_holder = {
        "name": "James Smith",
        "accountNumber": f"{random.randint(1000000000, 9999999999)}",
        "bankName": bank_name,
        "currency": "INR"
    }
    transactions = generate_transactions(start_balance=10000.0, num_transactions=50,
                                         start_date=start_date, end_date=end_date)

    return {
        "accountHolder": account_holder,
        "statementPeriod": {
            "startDate": start_date.strftime("%Y-%m-%d"),
            "endDate": end_date.strftime("%Y-%m-%d")
        },
        "transactions": transactions
    }

# Generate and print statement for HDFC Bank
hdfc_statement = generate_bank_statement("Axis Bank")
print(json.dumps(hdfc_statement, indent=2))
