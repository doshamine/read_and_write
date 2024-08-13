import os.path

def merge_and_sort(filenames: list) -> None:
	"""Объединяет файлы в один по следующим правилам:

    - Содержимое исходных файлов в результирующем файле отсортировано по количеству строк в них.
    - Содержимое каждого файла предваряется служебной информацией на 2-х строках: имя файла и количество строк в нем.
	
	Параметры:
	filenames -- список путей к текстовым файлам.

	Файл с результатом располагается в рабочем каталоге с именем result.txt
	"""
	string_amount_info = {}
	for filename in filenames:
		if not os.path.exists(filename):
			return f'Файл {filename} не существует.'

		string_amount_info[filename] = 0
		with open(filename) as f:
			while f.readline() != '':
				string_amount_info[filename] += 1
	string_amount_info = sorted(string_amount_info.items(), key=lambda item: item[1])
	
	with open('result.txt', 'w') as out_file:
		for filename, string_amount in string_amount_info:
			out_file.writelines([filename, '\n', str(string_amount), '\n'])
			
			with open(filename) as in_file:
				while out_file.write(in_file.readline()) != 0:
					pass
			out_file.write('\n\n')

if __name__ == '__main__':
	assert merge_and_sort(['1.txt', '2.txt', '5.txt']) == 'Файл 5.txt не существует.'
	merge_and_sort(['1.txt', '2.txt', '3.txt'])