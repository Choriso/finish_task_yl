from collections import Counter

with open("fake.txt", "r") as file:
    lines = file.read()

letters_with_R = []
for i, char in enumerate(lines):
    if char == "R":
        if i > 0:
            letters_with_R.append(lines[i - 1])
        if i < len(lines) - 1:
            letters_with_R.append(lines[i + 1])

if letters_with_R:
    chars_count = Counter(letters_with_R)
    max_count = max(chars_count.values())
    most_common_chars = [char for char, count in chars_count.items() if count == max_count]
    print("".join(most_common_chars))
else:
    print("В файле нет символа 'R' или он единственный в строке.")