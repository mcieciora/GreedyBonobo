import csv


class Payment:
    def __init__(self, payment_id, payment, description):
        self.payment_id = payment_id
        self.payment = payment
        self.description = description


def add_payment(payment, description):
    payment_list = get_payment_history()
    payment_list.append(Payment(get_next_payment_id(), payment, description))
    update_payment_history(payment_list)


def remove_payment(payment_id):
    payment_list = get_payment_history()
    for payment in payment_list:
        if payment.payment_id == payment_id:
            payment_list.remove(payment)
    update_payment_history(payment_list)


def update_payment_history(payment_list):
    open('payment.csv', 'w').close()
    with open('payment.csv', mode='a') as payment_history:
        history_writer = csv.writer(payment_history, delimiter='|')
        for payment in payment_list:
            history_writer.writerow([payment.payment_id, payment.payment, payment.description])


def get_next_payment_id():
    payment_history = get_payment_history()
    if len(payment_history) > 0:
        return int(payment_history[-1].payment_id) + 1
    else:
        return 1


def get_payment_id_list():
    payment_history = get_payment_history()
    payments_id_list = []
    for payment in payment_history:
        payments_id_list.append(payment.payment_id)
    return payments_id_list


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
