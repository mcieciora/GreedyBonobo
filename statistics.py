import Transaction as Trc
import Payment as Pmt
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
        print('Payment history:')
        for payment in Pmt.get_payment_history():
            print('{} - {}'.format(payment.payment, payment.description))
    else:
        print('There are no payments to show!')


def get_total_info():
    return 'Total: {} out of {} sum of limits ({}%)'.format(Trc.get_total(), ctg.get_total_of_limits(), get_percentage(
           Trc.get_total(), ctg.get_total_of_limits()))


def get_total_savings():
    savings = Pmt.get_total() - Trc.get_total()
    if Pmt.get_total() != 0:
        return 'Savings: {} out of {} total income ({}%)'.format(savings, Pmt.get_total(), get_percentage(savings,
                                                                                               Pmt.get_total()))
    else:
        return 'Savings: {} out of {} total income ({}%)'.format(savings, Pmt.get_total(), 0)


def get_total_categories():
    print('Total by categories: ')
    for category in ctg.get_categories_names():
        if Trc.get_total() != 0:
            print('{}: {} of {} limit which is {}% of total spends'.format(category, Trc.get_total_by_category(
                category),
                ctg.get_category_limit(category), get_percentage(Trc.get_total_by_category(category), Trc.get_total())))
        else:
            print('{}: {} of {} limit which is {}% of total spends'.format(category, Trc.get_total_by_category(
                category), ctg.get_category_limit(
                category), 0))


def get_percentage(a, b):
    return round(a/b*100, 2)
