# Нарисовать равнобедренный треугольник из символов ^. Высоту выбирает пользователь. Например: высота = 5, на экране

num = int(input('insert number of lines: '))
for i in range(1, (num + 1)):
    line_pic = i * '/\\'
    print(line_pic.center(num*2, ' '))