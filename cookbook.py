from pprint import pprint


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


cook_book = catalog_reader('recipe.txt')
print(cook_book)