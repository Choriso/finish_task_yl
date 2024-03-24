import csv
import json

# Чтение данных из файла worlds.csv
worlds_data = []
with open('worlds.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter='&')
    next(csv_reader)  # Пропускаем заголовки
    for row in csv_reader:
        worlds_data.append(row)

# Обработка данных и формирование словаря слабых мест
weaknesses_dict = {}
for entry in worlds_data:
    world = entry[1].strip()  # Название мира
    weakness = entry[3].strip()  # Слабость
    place = entry[2].strip()  # Место
    if world not in weaknesses_dict:
        weaknesses_dict[world] = []
    weaknesses_dict[world].append([weakness, place])

# Сортировка списков слабых мест для каждого мира
for world, spots in weaknesses_dict.items():
    spots.sort()

# Запись словаря в файл thin_spot.json
with open('thin_spot.json', 'w') as jsonfile:
    json.dump(weaknesses_dict, jsonfile, ensure_ascii=False, indent=4)