import Transaction as Trc
import Payment as Pmt
import Period as Prd
import categories as ctg


def show_history():
    if len(Trc.get_transaction_history()) > 0:
        print('Transactions history:')
        for transaction in Trc.get_transaction_history():
            print('&{} {}PLN for {} - {}'.format(transaction.transaction_id, transaction.expense, transaction.category,
                                                 transaction.description))
    else:
        print('There are no transactions to show!')
    if len(Pmt.get_payment_history()) > 0:
        print('Income history:')
        for payment in Pmt.get_payment_history():
            print('&{} {} - {}'.format(payment.payment_id, payment.payment, payment.description))
    else:
        print('There are no incomes to show!')


def get_total_info():
    return 'Total: {} out of {} sum of limits ({}%)'.format(Trc.get_total(), ctg.get_total_of_limits(), get_percentage(
           Trc.get_total(), ctg.get_total_of_limits()))


def get_total_savings():
    savings = round(Pmt.get_total() - Trc.get_total(), 2)
    return 'Savings: {} out of {} total income ({}%)'.format(savings, Pmt.get_total(), get_percentage(savings,
                                                                                                      Pmt.get_total()))


def show_history_sorted_descending():
    if len(Trc.get_transaction_history()) > 0:
        print('Transactions history [cost descending]:')
        sorted_list = sorted(Trc.get_transaction_history(), key=lambda x: float(x.expense), reverse=True)
        for transaction in sorted_list:
            print('&{} {}PLN for {} - {}'.format(transaction.transaction_id, transaction.expense, transaction.category,
                                                 transaction.description))
    else:
        print('There are no transactions to show!')
    if len(Pmt.get_payment_history()) > 0:
        print('Income history [cost descending]:')
        sorted_list = sorted(Pmt.get_payment_history(), key=lambda x: x.payment, reverse=True)
        for payment in sorted_list:
            print('&{} {} - {}'.format(payment.payment_id, payment.payment, payment.description))
    else:
        print('There are no incomes to show!')


def show_history_group_by_categories():
    if len(Trc.get_transaction_history()) > 0:
        print('Transactions history [group by categories]:')
        sorted_list = sorted(Trc.get_transaction_history(), key=lambda x: x.category, reverse=False)
        for transaction in sorted_list:
            print('&{} {}PLN for {} - {}'.format(transaction.transaction_id, transaction.expense, transaction.category,
                                                 transaction.description))
    else:
        print('There are no transactions to show!')
    if len(Pmt.get_payment_history()) > 0:
        print('Income history:')
        for payment in Pmt.get_payment_history():
            print('&{} {} - {}'.format(payment.payment_id, payment.payment, payment.description))
    else:
        print('There are no incomes to show!')


def get_basic_info():
    print('\nActual period: {}'.format(Prd.get_actual_period_name()))
    print('Total expenses: {}/{} ({}%)'.format(Trc.get_total(), ctg.get_total_of_limits(), get_percentage(
        Trc.get_total(), ctg.get_total_of_limits())))
    print('Incomes: {}\n'.format(Pmt.get_total()))


def get_total_by_category(category):
    print('    {} of {} limit ({}%) which is {}% of total expenses'.format(Trc.get_total_by_category(
        category), ctg.get_category_limit(category), get_percentage(Trc.get_total_by_category(category),
                                                                    ctg.get_category_limit(category)),
        get_percentage(Trc.get_total_by_category(category), Trc.get_total())))


def get_average_by_category(category):
    if len(Trc.get_transactions_by_category(category)) > 0:
        print('    Average expanse per transaction is {}'.format(Trc.get_total_by_category(category)/len(
            Trc.get_transactions_by_category(category))))


def print_biggest_expanse():
    biggest = get_biggest_expanse()
    if biggest is not None:
        print('Biggest expanse: {} for {} - {}'.format(biggest.expense, biggest.category, biggest.description))
    else:
        print('Biggest expanse: no transactions')


def get_biggest_expanse():
    transaction_list = Trc.get_transaction_history()
    if len(transaction_list) > 0:
        biggest = transaction_list[0]
        for transaction in transaction_list:
            if float(transaction.expense) > float(biggest.expense):
                biggest = transaction
        return biggest


def print_biggest_expanse_by_category(category):
    biggest = get_biggest_expanse_by_category(category)
    if biggest is not None:
        print('    Biggest expanse in category: {} - {}'.format(biggest.expense, biggest.description))
    else:
        print('    Biggest expanse in category: no transactions')


def get_biggest_expanse_by_category(category):
    transaction_list = Trc.get_transactions_by_category(category)
    if len(transaction_list) > 0:
        biggest = transaction_list[0]
        for transaction in transaction_list:
            if float(transaction.expense) > float(biggest.expense):
                biggest = transaction
        return biggest


def get_percentage(a, b):
    if b > 0:
        return round(a/b*100, 2)
    else:
        return 0
