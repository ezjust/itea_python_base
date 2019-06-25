# Дано натуральное число N. Выведите слово YES
# если число N является точной степенью двойки, или слово NO в противном случае.

number = int(input('insert number: '))
for i in range(0, 64):
    if number == 2**i:
        print("YES")
        exit()
print("NO")


