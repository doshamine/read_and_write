import os.path

def create_cookbook(filename: str) -> dict:
	"""Преобразует данные о блюдах из форматированного файла в словарь.
	
	Параметры:
	filename -- путь к текстовому файлу. Данные о блюдах должны быть разделены
	одной пустой строкой и быть отформатированными следующим образом:
	Омлет
	3
	Яйцо | 2 | шт
	Молоко | 100 | мл
	Помидор | 2 | шт

	Возвращаемое значение:
	Словарь, содержащий пары в формате
	'Омлет': [
		{'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт'},
		{'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
		{'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ]
	"""
	if not os.path.exists(filename):
		return f'Файл {filename} не существует.'

	cookbook = {}
	with open(filename) as f:
		while True:
			dish = f.readline().rstrip()   
			if not dish:
				break
			cookbook[dish] = []

			ingredients_number = int(f.readline().rstrip()) 

			for i in range(ingredients_number):
				name, quantity, measure = f.readline().rstrip().split(' | ')
				cookbook[dish].append({'ingredient_name': name, 'quantity': int(quantity), 'measure': measure})

			f.readline()

	return cookbook


if __name__ == '__main__':
	desired_cookbook = {
		'Омлет': [
			{'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт'},
			{'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
			{'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    	],
		'Утка по-пекински': [
			{'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
			{'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
			{'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
			{'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
		],
		'Запеченный картофель': [
			{'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
			{'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
			{'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'}
		],
		'Фахитос': [
			{'ingredient_name': 'Говядина', 'quantity': 500, 'measure': 'г'},
			{'ingredient_name': 'Перец сладкий', 'quantity': 1, 'measure': 'шт'},
			{'ingredient_name': 'Лаваш', 'quantity': 2, 'measure': 'шт'},
			{'ingredient_name': 'Винный уксус', 'quantity': 1, 'measure': 'ст.л'},
			{'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    	]
	}

	not_cookbook = create_cookbook('recepty.txt')
	assert not_cookbook == 'Файл recepty.txt не существует.'
	
	cookbook = create_cookbook('recipes.txt')
	assert cookbook == desired_cookbook
