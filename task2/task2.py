def get_shop_list_by_dishes(dishes: list, person_count: int) -> dict:
	"""Составляет список покупок.
	
	Параметры:
	dishes -- список названий блюд.
	person_count -- количество человек.

	Возвращаемое значение:
	Словарь с названием ингредиентов и их необходимым количеством.
	"""
	shop_list = {}

	with open('recipes.txt') as f:
		dish_counter = 0

		while True:
			if dish_counter == len(dishes):
				break

			dish = f.readline().rstrip()   
			if not dish:
				if dish_counter < len(dishes):
					return 'Ошибка. В списке есть неизвестное блюдо.'
				break

			if dish not in dishes:
				while f.readline().rstrip() != '':
					pass
				continue

			ingredients_number = int(f.readline().rstrip())

			for i in range(ingredients_number):
				name, quantity, measure = f.readline().rstrip().split(' | ')
				shop_list.setdefault(name, {'measure': measure, 'quantity': 0})
				shop_list[name]['quantity'] += int(quantity) * person_count

			f.readline()
			dish_counter += 1

	return shop_list


if __name__ == '__main__':
	shop_list_bad = get_shop_list_by_dishes(['Утка по-пекински', 'Борстч'], 4)
	shop_list_good = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

	assert shop_list_bad == 'Ошибка. В списке есть неизвестное блюдо.'
	assert shop_list_good == {
	  'Картофель': {'measure': 'кг', 'quantity': 2},
	  'Молоко': {'measure': 'мл', 'quantity': 200},
	  'Помидор': {'measure': 'шт', 'quantity': 4},
	  'Сыр гауда': {'measure': 'г', 'quantity': 200},
	  'Яйцо': {'measure': 'шт', 'quantity': 4},
	  'Чеснок': {'measure': 'зубч', 'quantity': 6}
	}


