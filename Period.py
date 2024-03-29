from datetime import datetime
from datetime import date
import csv
import Payment as Ptm
import Transaction as Trc
import categories as ctg


class Period:
    def __init__(self, name, incomes, spendings, savings, categories, date, active):
        self.name = name
        self.incomes = incomes
        self.spendings = spendings
        self.savings = savings
        self.categories = categories
        self.date = date
        self.active = active


def start_period():
    period_name = input('Insert period name: ')
    if period_name not in get_periods_names():
        add_period(Period(period_name, 0, 0, 0, [], datetime.today().strftime('%d-%m-%Y'), True))
        print('Period started successfully!')
    else:
        print('There is already period with that name!')
        return start_period()


def close_period():
    answer = input('Are you sure you want to close {} period? [Y/n] '.format(get_actual_period_name()))
    if answer.lower() == 'y':
        current_period = get_actual_period_name()
        update_history(current_period)
        open('period.csv', 'w').close()
        open('payment.csv', 'w').close()
        print('Period {} closed successfully!'.format(current_period))
    elif answer.lower() == 'n':
        pass
    else:
        print('Please insert proper answer!')
        return close_period()


def update_history(period_name):
    incomes = Ptm.get_total()
    spendings = Trc.get_total()
    savings = incomes - spendings
    remove_period(period_name)
    categories = []
    for category in ctg.get_categories_names():
        categories.append('{}={}/{}'.format(category, Trc.get_total_by_category(category),
                                            ctg.get_category_limit(category)))
    add_period(Period(period_name, incomes, spendings, savings, categories, datetime.today().strftime('%d-%m-%Y'),
                      False))


def add_period(period):
    period_list = get_periods_list()
    period_list.append(period)
    save_period_info(period_list)


def remove_period(period_name):
    period_list = get_periods_list()
    for period in period_list:
        if period.name == period_name:
            period_list.remove(period)
    save_period_info(period_list)


def remove_period_from_history(period_name):
    if period_name != get_actual_period_name():
        period_list = get_periods_list()
        for period in period_list:
            if period.name == period_name:
                period_list.remove(period)
        save_period_info(period_list)
        print('Period removed successfully!')
    else:
        print('Current period cannot be removed!')


def save_period_info(period_list):
    open('history.csv', 'w').close()
    with open('history.csv', mode='a') as periods_info_file:
        for period in period_list:
            csv_writer = csv.writer(periods_info_file, delimiter='|')
            csv_writer.writerow([period.name, period.incomes, period.spendings, period.savings, period.categories,
                                 period.date, period.active])


def get_periods_list():
    period_list = []
    with open('history.csv', mode='r') as period_info_file:
        for row in period_info_file.readlines():
            if row != '\n':
                split_row = row.replace('\n', '').split('|')
                period_list.append(Period(split_row[0], split_row[1], split_row[2], split_row[3], split_row[4],
                                          split_row[5], split_row[6]))
    return period_list


def get_periods_names():
    period_list = get_periods_list()
    period_names = []
    for period in period_list:
        period_names.append(period.name)
    return period_names


def get_actual_period_name():
    if is_period_active():
        return get_periods_names()[-1]
    else:
        return 'None'


def is_period_active():
    if len(get_periods_list()) > 0 and get_periods_list()[-1].active == 'True':
        return True
    else:
        return False


def get_period_day_number():
    if is_period_active():
        current_date = datetime.today().date()
        date_object = datetime.strptime(get_periods_list()[-1].date, '%d-%m-%Y').date()
        delta = current_date - date_object
        return delta.days
    else:
        return 'None'
