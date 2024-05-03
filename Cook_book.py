cook_book = {}
with open("recipes.txt", encoding='utf-8') as file:
    key = ''
    for line in file:
        line = line.strip()
        if line.isdigit():
            continue
        elif line and '|' not in line:
            cook_book[line] = []
            key = line
        elif line and '|' in line:
            ingredient, quantity, measure = line.split(" | ")
            cook_book.get(key).append(dict(ingredient_name=ingredient, quantity=int(quantity), measure=measure))

from pprint import pprint

pprint(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    for ingr in cook_book[dish]:
      ingredient = ingr['ingredient_name']
      quantity = ingr['quantity'] * person_count
      measure = ingr['measure']
      if ingredient in shop_list:
        shop_list[ingredient]['quantity'] += quantity
      else:
        shop_list[ingredient] = {'quantity': quantity, 'measure': measure}
  print(shop_list)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
