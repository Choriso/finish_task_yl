from flask import Flask, jsonify
import json
import sqlite3

app = Flask(__name__)

# Загрузка данных из файла fear.json
with open("fear.json", "r") as file:
    fear_data = json.load(file)


@app.route('/fear', methods=['GET'])
def get_advices():
    # Установка соединения с базой данных
    conn = sqlite3.connect(fear_data["filename"])
    cursor = conn.cursor()

    # Формирование SQL-запроса для выборки советов
    sql_query = "SELECT fear, advice, level FROM Advices WHERE fear IN ({}) AND level >= {}".format(
        ', '.join('?' * len(fear_data["fears"])), fear_data["level"]
    )

    # Выполнение SQL-запроса и получение результатов
    cursor.execute(sql_query, fear_data["fears"])
    advices = cursor.fetchall()

    # Закрытие соединения с базой данных
    conn.close()

    # Сортировка списка советов по алфавиту
    sorted_advices = sorted(advices, key=lambda x: x[1])

    # Формирование списка словарей для вывода
    result = [{'fear': advice[0], 'advice': advice[1], 'level': advice[2]} for advice in sorted_advices]

    return jsonify(result)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)