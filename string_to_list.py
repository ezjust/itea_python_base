# Напишите программу, которая преобразует строку, в которой записаны слова через “,” в список из этих слов

text = 'one, two, three, five, 11, eleven'
text_list = list(text.split(','))
print(text_list)
