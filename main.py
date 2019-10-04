import sys
import os
import Transaction as Trc
import Payment as Pmt
import Period as Prd
import utilities as uti
import categories as ctg
import statistics as stat


def main_menu():
    stat.get_basic_info()
    print('[1] Add/Remove transaction\n[2] Add/Remove income\n[3] Show history\n[4] Show statistics\n[5] '
          'Add/Remove '
          'category\n[6] Update limits\n[7] Manage periods\n')
    menu_change(input('>>>'))


def back_to_main_menu():
    input('...')


def add_transaction():
    if Prd.is_period_active():
        answer = input('Would you like to [a]add or [r]remove transaction? ')
        if answer.lower() == 'a':
            Trc.add_transaction(uti.get_expanse(), uti.get_description(), uti.get_category())
            print('Transaction added successfully!')
        elif answer.lower() == 'r':
            transaction_id = input('Insert transaction &id: ')
            if transaction_id in Trc.get_transactions_id_list():
                Trc.remove_transaction(transaction_id)
                print('Transaction removed successfully!')
            else:
                print('There is no transaction with such &id!')
                return add_transaction()
        elif answer.lower() == 'q':
            main_menu()
        else:
            print('There is no such option. Please choose proper one!')
            return add_transaction()
    else:
        print('There is no active period!')
    back_to_main_menu()


def add_income():
    if Prd.is_period_active():
        answer = input('Would you like to [a]add or [r]remove income? ')
        if answer.lower() == 'a':
            Pmt.add_payment(uti.get_payment(), uti.get_description())
            print('Income added successfully!')
        elif answer.lower() == 'r':
            payment_id = input('Insert income &id: ')
            if payment_id in Pmt.get_payment_id_list():
                Pmt.remove_payment(payment_id)
                print('Income removed successfully!')
            else:
                print('There is no income with such &id!')
                return add_income()
        elif answer.lower() == 'q':
            main_menu()
        else:
            print('There is no such option. Please choose proper one!')
            return add_transaction()
    else:
        print('There is no active period!')
    back_to_main_menu()


def history():
    if Prd.is_period_active():
        answer = input('Would you like to show [f]full history, [s]sort descending or [g]group by categories? ')
        if answer.lower() == 'f':
            stat.show_history()
        elif answer.lower() == 's':
            stat.show_history_sorted_descending()
        elif answer.lower() == 'g':
            stat.show_history_group_by_categories()
        elif answer.lower() == 'q':
            main_menu()
        else:
            print('There is no such option. Please choose proper one!')
            return history()
    else:
        print('There is no active period!')
    back_to_main_menu()


def add_remove_category():
    if Prd.is_period_active() is False:
        print(*ctg.get_categories_names())
        answer = input('Would you like to [a]add or [r]remove category? ')
        if answer.lower() == 'a':
            ctg.add_category()
            print(*ctg.get_categories_names())
        elif answer.lower() == 'r':
            ctg.remove_category()
            print(*ctg.get_categories_names())
        elif answer.lower() == 'q':
            main_menu()
        else:
            print('There is no such option. Please choose proper one!')
            return add_remove_category()
    else:
        print('Categories cannot be modified when period is active!')
    back_to_main_menu()


def update_limits():
    if Prd.is_period_active() is False:
        print(*ctg.get_categories_list())
        answer = input('Which category limit would you like to update? ')
        if answer in ctg.get_categories_names():
            ctg.update_category_limit(answer)
        elif answer.lower() == 'q':
            main_menu()
        else:
            print('There is no such category!')
            return update_limits()
    else:
        print('Categories cannot be modified when period is active!')
    back_to_main_menu()


def manage_periods():
    print('Actual period: {}'.format(Prd.get_actual_period_name()))
    answer = input('Would you like to [l]list, [s]start, [c]close or [r]remove periods? ')
    if answer.lower() == 's':
        if Prd.is_period_active() is False:
            Prd.start_period()
        else:
            print('There is already active period!')
    elif answer.lower() == 'c':
        if Prd.is_period_active():
            Prd.close_period()
        else:
            print('There is no active period to close!')
    elif answer.lower() == 'q':
        main_menu()
    elif answer.lower() == 'l':
        if len(Prd.get_periods_list()) > 0:
            print(Prd.get_periods_names())
        else:
            print('There are no periods to list!')
    elif answer.lower() == 'r':
        print(*Prd.get_periods_names())
        period_name = input('Insert period name to remove: ')
        if period_name in Prd.get_periods_names():
            Prd.remove_period_from_history(period_name)
        else:
            print('There is no period with such name!')
            return manage_periods()
    else:
        print('There is no such option. Please choose proper one!')
        return manage_periods()
    back_to_main_menu()


def statistics():
    if Prd.is_period_active():
        print('Actual period: {}'.format(Prd.get_actual_period_name()))
        print('Actual period day: '.format(Prd.get_period_day_number()))
        print('Available categories: {}'.format([*ctg.get_categories_names()]))
        print(stat.get_total_info())
        print(stat.get_total_savings())
        stat.print_biggest_expanse()
        for category in ctg.get_categories_names():
            print('-{}:'.format(category))
            stat.get_total_by_category(category)
            stat.print_biggest_expanse_by_category(category)
            stat.get_average_by_category(category)
    else:
        print('There is no active period!')
    back_to_main_menu()


def validate_environment():
    files = ['period.csv', 'payment.csv', 'history.csv', 'categories']
    for file in files:
        if not os.path.isfile(file):
            open(file, 'w')
    main_menu()


def menu_change(choice):
    if choice.lower() == 'q':
        sys.exit()
    elif choice in menu_map.keys():
        menu_map[choice]()
    else:
        print('There is no such option, please insert proper one!')
    main_menu()


menu_map = {
    '1': add_transaction,
    '2': add_income,
    '3': history,
    '4': statistics,
    '5': add_remove_category,
    '6': update_limits,
    '7': manage_periods
}

validate_environment()
