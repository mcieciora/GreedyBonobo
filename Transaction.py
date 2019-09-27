import csv


class Transaction:
    def __init__(self, transaction_id, expense, description, category):
        self.transaction_id = transaction_id
        self.expense = expense
        self.description = description
        self.category = category


def add_transaction(expanse, description, category):
    transactions_list = get_transaction_history()
    transactions_list.append(Transaction(get_next_transaction_id(), expanse, description, category))
    update_transactions_history(transactions_list)


def remove_transaction(transaction_id):
    transaction_list = get_transaction_history()
    for transaction in transaction_list:
        if transaction.transaction_id == transaction_id:
            transaction_list.remove(transaction)
    update_transactions_history(transaction_list)


def update_transactions_history(transaction_list):
    open('period.csv', 'w').close()
    with open('period.csv', mode='a') as transaction_history:
        history_writer = csv.writer(transaction_history, delimiter='|')
        for transaction in transaction_list:
            history_writer.writerow([transaction.transaction_id, transaction.expense, transaction.description,
                                    transaction.category])


def get_next_transaction_id():
    transaction_history = get_transaction_history()
    if len(transaction_history) > 0:
        return int(transaction_history[-1].transaction_id) + 1
    else:
        return 1


def get_transactions_id_list():
    transaction_history = get_transaction_history()
    transactions_id_list = []
    for transaction in transaction_history:
        transactions_id_list.append(transaction.transaction_id)
    return transactions_id_list


def get_transactions_by_category(category):
    transaction_history = get_transaction_history()
    category_list = []
    for transaction in transaction_history:
        if transaction.category == category:
            category_list.append(transaction)
    return category_list


def get_transaction_history():
    transaction_history = []
    with open('period.csv', mode='r') as history_file:
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
