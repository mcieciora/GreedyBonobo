import Transaction as Trc


def add_category():
    new_category = input('Insert new category name: ')
    categories_list = get_categories_list()
    if new_category not in get_categories_names():
        category_limit = get_category_limit()
        categories_list.append('{}={}'.format(new_category, category_limit))
        update_category_file(categories_list)
        print('Category added successfully!')
    else:
        print('There is already category with such name!')
        return add_category()


def remove_category():
    print(*get_categories_names())
    category_to_remove = input('Insert category to remove: ')
    categories_list = get_categories_list()
    if category_to_remove in get_categories_names():
        for category in categories_list:
            if category.startswith(category_to_remove):
                categories_list.remove(category)
                update_category_file(categories_list)
                print('Category removed successfully!')
    else:
        print('No such category!')
        return remove_category()


def get_categories_list():
    categories_list = []
    with open('categories', mode='r') as categories_file:
        for row in categories_file.readlines():
            categories_list.append(row.replace('\n', ''))
    return categories_list


def get_categories_names():
    categories_list = []
    with open('categories', mode='r') as categories_file:
        for row in categories_file.readlines():
            categories_list.append(row.replace('\n', '').split('=')[0])
    return categories_list


def update_category_file(new_category_list):
    open('categories', 'w').close()
    with open('categories', mode='a') as categories_file:
        categories_file.writelines([category + '\n' for category in new_category_list])


def get_category_limit():
    try:
        limit = float(input('Please insert new category limit: '))
    except ValueError:
        print('Input should be a number!')
        return get_category_limit()
    if limit <= 0:
        print('Input should be positive!')
        return get_category_limit()
    return limit


def get_total_of_limits():
    limits_list = get_categories_list()
    total = 0
    for limit in limits_list:
        total += float(limit.split('=')[1])
    return total


def get_total_percentage():
    return round(Trc.get_total()/get_total_of_limits()*100, 2)
