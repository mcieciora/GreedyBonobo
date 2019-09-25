import csv


class Transaction:
    def __init__(self, transaction_id, expense, description, category):
        self.transaction_id = transaction_id
        self.expense = expense
        self.description = description
        self.category = category


def create_transaction(expense, description, category):
    with open('history.csv', mode='a') as history_file:
        history_writer = csv.writer(history_file, delimiter='|')
        history_writer.writerow([get_next_transaction_id(), expense, description, category])


def get_next_transaction_id():
    transaction_history = get_transaction_history()
    if len(transaction_history) > 0:
        return int(transaction_history[-1].transaction_id) + 1
    else:
        return 1


def get_transactions_by_category(category):
    transaction_history = get_transaction_history()
    category_list = []
    for transaction in transaction_history:
        if transaction.category == category:
            category_list.append(transaction)
    return category_list


def get_transaction_history():
    transaction_history = []
    with open('history.csv', mode='r') as history_file:
        history = history_file.readlines()
        for row in history:
            split_row = row.replace('\n', '').split('|')
            transaction_history.append(Transaction(split_row[0], split_row[1], split_row[2], split_row[3]))
    return transaction_history


def get_total():
    transaction_history = get_transaction_history()
    total = 0
    for transaction in transaction_history:
        total += float(transaction.expense)
    return round(total, 2)


def get_total_by_category(category):
    transaction_history = get_transaction_history()
    total = 0
    for transaction in transaction_history:
        if transaction.category == category:
            total += float(transaction.expense)
    return round(total, 2)


def get_biggest_expanse():
    transaction_history = get_transaction_history()
    biggest = None
    if len(transaction_history) > 0:
        biggest = transaction_history[0]
        for transaction in transaction_history:
            if transaction.expense > biggest.expense:
                biggest = transaction
    return biggest
