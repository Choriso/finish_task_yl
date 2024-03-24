from flask import Flask, jsonify

app = Flask(__name__)

# Данные о мирах с их мыслями
worlds_data = [
  {
    "name": "Mack",
    "dreams": [
      [
        "What for?",
        33
      ],
      [
        "Busy.",
        46
      ],
      [
        "Are you sure you want to know?",
        28
      ],
      [
        "Of course.",
        23
      ]
    ]
  },
  {
    "name": "Henry",
    "dreams": [
      [
        "Are you sure you want to know?",
        12
      ],
      [
        "Busy.",
        64
      ],
      [
        "That says it all.",
        25
      ],
      [
        "Which was exactly what needed to be proved.",
        24
      ]
    ]
  },
  {
    "name": "Toop",
    "dreams": [
      [
        "Is it really not clear?!",
        10
      ],
      [
        "It's brilliant!",
        68
      ],
      [
        "Which was exactly what needed to be proved.",
        27
      ],
      [
        "That's right.",
        4
      ]
    ]
  },
  {
    "name": "Tim",
    "dreams": [
      [
        "How long?",
        87
      ],
      [
        "YES",
        9
      ],
      [
        "Busy.",
        13
      ],
      [
        "Is it really not clear?!",
        65
      ]
    ]
  },
  {
    "name": "Yavor",
    "dreams": [
      [
        "That says it all.",
        7
      ],
      [
        "Why?",
        93
      ],
      [
        "How long?",
        5
      ]
    ]
  },
  {
    "name": "Woolly",
    "dreams": [
      [
        "What for?",
        85
      ],
      [
        "Of course.",
        18
      ],
      [
        "That's right.",
        20
      ],
      [
        "It's brilliant!",
        5
      ]
    ]
  }
]


@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(worlds_data)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)