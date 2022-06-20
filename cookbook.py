def catalog_reader(file_name):
    with open(file_name, encoding='utf-8') as file:
        result = {}
        for line in file:
            cook_name = line.strip()
            components_qty = file.readline()
            ingredients = []
            for item in range(int(components_qty)):
                ingredient = file.readline()
                ingredients.append(ingredient.strip())
            ingredients_list = []
            for ingred in ingredients:
                ingredients_split = ingred.split(' | ')
                ingredients_dict = {'ingredient_name': ingredients_split[0], 'quantity': ingredients_split[1],
                                    'measure': ingredients_split[2]}
                ingredients_list.append(ingredients_dict)
            result[cook_name] = ingredients_list
            file.readline()
        return result


def get_shop_list_by_dishes(dishes, person_count):
    menu_order = {}
    dishes_list = dishes
    for dish in dishes_list:
        if dish in cook_book:
            for name in cook_book[dish]:
                if name['ingredient_name'] in menu_order:
                    menu_order[name['ingredient_name']]['quantity'] += (int(name['quantity']) * int(person_count))

                else:
                    menu_components = {'measure': name['measure'],
                                       'quantity': int(name['quantity']) * int(person_count)}
                    menu_order[name['ingredient_name']] = menu_components
        else:
            print(f'Блюда "{dish}" нет в меню')

    print(menu_order)


cook_book = catalog_reader('recipe.txt')
print(cook_book)
print()

get_shop_list_by_dishes(['Запеченный картофель', 'Запеченный картофель', 'Омлет'], 3)