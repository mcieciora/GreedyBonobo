import csv
import Payment as Ptm
import Transaction as Trc


class Period:
    def __init__(self, name, incomes, spendings, savings, active):
        self.name = name
        self.incomes = incomes
        self.spendings = spendings
        self.savings = savings
        self.active = active


def start_period():
    period_name = input('Insert period name: ')
    if period_name not in get_periods_names():
        add_period(Period(period_name, 0, 0, 0, True))
    else:
        print('There is already period with that name!')
        return start_period()


def close_period():
    answer = input('Are you sure you want to close actual period? [Y/n] ')
    if answer.lower() == 'y':
        update_history(get_actual_period_name())
        open('period.csv', 'w').close()
        open('payment.csv', 'w').close()
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
    add_period(Period(period_name, incomes, spendings, savings, False))


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


def save_period_info(period_list):
    open('history.csv', 'w').close()
    with open('history.csv', mode='a') as periods_info_file:
        for period in period_list:
            csv_writer = csv.writer(periods_info_file, delimiter='|')
            csv_writer.writerow([period.name, period.incomes, period.spendings, period.savings, period.active])


def get_periods_list():
    period_list = []
    with open('history.csv', mode='r') as period_info_file:
        for row in period_info_file.readlines():
            split_row = row.replace('\n', '').split('|')
            period_list.append(Period(split_row[0], split_row[1], split_row[2], split_row[3], split_row[4]))
    return period_list


def get_periods_names():
    period_list = get_periods_list()
    period_names = []
    for period in period_list:
        period_names.append(period.name)
    return period_names


def get_actual_period_name():
    return get_periods_names()[-1]


def is_period_active():
    if len(get_periods_list()) > 0 and get_periods_list()[-1].active == 'True':
        return True
    else:
        print('There is no active period!')
        return False