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


def get_basic_info():
    print('\nActual period: {}'.format(Prd.get_actual_period_name()))
    print('Total expenses: {}/{} ({}%)'.format(Trc.get_total(), ctg.get_total_of_limits(), get_percentage(
        Trc.get_total(), ctg.get_total_of_limits())))
    print('Incomes: {}\n'.format(Pmt.get_total()))


def get_total_categories():
    print('Total by categories: ')
    for category in ctg.get_categories_names():
        print('-{}:\n    {} of {} limit ({}%) which is {}% of total expenses'.format(category,
            Trc.get_total_by_category(category), ctg.get_category_limit(category), get_percentage(
                Trc.get_total_by_category(category), ctg.get_category_limit(category)),
                                                                            get_percentage(
                Trc.get_total_by_category(category), Trc.get_total())))


def get_percentage(a, b):
    if b > 0:
        return round(a/b*100, 2)
    else:
        return 0
