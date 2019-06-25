# Организовать непрерывный ввод цифр с клавиатуры, пока пользователь НЕ введёт 0
# После ввода нуля, показать на экран количество чисел,
# которые были Введены, их общую сумму и среднее арифметическое.

i = int(input('input any int: '))
v_list = []
while i != 0:
    i = int(input('input any int: '))
    v_list.append(i)
print('list length: ', (len(v_list)))
sum = 0
for num in v_list:
    sum = sum + num
print('sum of elements in the list: ', sum)
print('average value from the list is:', sum/len(v_list))
