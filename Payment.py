import csv


class Payment:
    def __init__(self, payment_id, payment, description):
        self.payment_id = payment_id
        self.payment = payment
        self.description = description


def create_payment(payment, description):
    with open('payment.csv', mode='a') as payment_file:
        payment_writer = csv.writer(payment_file, delimiter='|')
        payment_writer.writerow([get_next_payment_id(), payment, description])


def get_next_payment_id():
    payment_history = get_payment_history()
    if len(payment_history) > 0:
        return int(payment_history[-1].payment_id) + 1
    else:
        return 1


def get_payment_history():
    payment_history = []
    with open('payment.csv', mode='r') as payment_file:
        payments = payment_file.readlines()
        for row in payments:
            split_row = row.replace('\n', '').split('|')
            payment_history.append(Payment(split_row[0], split_row[1], split_row[2]))
    return payment_history


def get_total():
    payment_history = get_payment_history()
    total = 0
    for payment in payment_history:
        total += float(payment.payment)
    return round(total, 2)
