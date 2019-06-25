# Выводить буквы строки, до первой заглавной

string_1 = 'inserted any string With one uppercase letter'
for letter in string_1:
    if letter.isupper():
        break
    else:
        print(letter, end='')
