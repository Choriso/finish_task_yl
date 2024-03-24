import csv

def filter_changes(database_file, max_speed, forbidden_word, output_file):
    # Устанавливаем соединение с базой данных SQLite
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()

    # Выполняем SQL-запрос для выборки данных из таблицы Changes
    cursor.execute("SELECT * FROM Changes")

    # Получаем все строки результата запроса
    changes = cursor.fetchall()

    # Фильтруем изменения в соответствии с условиями
    filtered_changes = []
    for change in changes:
        if int(change['speed']) < max_speed and forbidden_word not in change['change']:
            filtered_changes.append({
                'no': change['id'],
                'change': change['change'],
                'type': change['type_id'],
                'world': change['world']
            })

    # Записываем отфильтрованные изменения в новый файл
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['no', 'change', 'type', 'world', 'relevance'], delimiter='#')
        writer.writeheader()
        for change in filtered_changes:
            writer.writerow(change)

# Пример использования функции
filter_changes('database.csv', 100, 'unreal', 'unreal.csv')