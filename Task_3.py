import requests      # Импортируем библиотеку для работы с HTTP-запросами
def notion_in_face(letters,  *, server=('127.0.0.1', 5000), font=12):
    data = get_data_from_server(server)
    if data:
        # Фильтрация данных по условиям задачи
        selected_people = []
        for person in data:
            if any(letter.lower() in person["name"].lower() for letter in letters):
                for dream, dream_font in person["dreams"]:
                    if dream_font >= font:
                        selected_people.append([person["name"], dream])

        # Сортировка списка по длине мысли и имени
        selected_people.sort(key=lambda x: (-len(x[1]), x[0]))

        return selected_people
def get_data_from_server(server):
    url = f"http://{server[0]}:{server[1]}/data"  # Формируем URL для запроса данных
    response = requests.get(url)  # Отправляем GET-запрос на сервер
    if response.status_code == 200:  # Проверяем успешность запроса
        data = response.json()  # Получаем данные в формате JSON
        return data
    else:
        print("Ошибка при получении данных с сервера")
        return None
result = notion_in_face('Thought', font=33)
print(result)