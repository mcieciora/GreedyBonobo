import categories as ctg


def get_expanse():
    try:
        expanse = float(input('Please insert expanse value: '))
    except ValueError:
        print('Input should be a number!')
        return get_expanse()
    if expanse <= 0:
        print('Input should be positive!')
        return get_expanse()
    return expanse


def get_payment():
    try:
        payment = float(input('Please insert income value: '))
    except ValueError:
        print('Input should be a number')
        return get_payment()
    if payment <= 0:
        print('Input should be positive!')
        return get_payment()
    return payment


def get_category():
    print(*ctg.get_categories_names())
    category = input('Please insert category: ')
    if category not in ctg.get_categories_names():
        print('There is no such category. Please choose proper one!')
        return get_category()
    return category


def get_description():
    description = input('Please insert short description: ')
    if len(description) == 0:
        print('Description cannot be empty!')
        return get_description()
    return description
