# По данному числу n закончите фразу «На лугу пасется...» одним из возможных продолжений:
# «n коров», «n корова», «n коровы», правильно склоняя слово «корова».
# Формат входных данных
# Дано целое положительное число n
# Формат выходных данных
# Программа должна вывести введенное число n и одно из слов (на латинице):
# коров, корова или коровы
# Например, 1 корова, 2 коровы, 5 коров, 125 коров.

# TODO: your code here

n = int(input("На лугу пасется..."))
if n <= 0:
    print("Коров нет")

elif n % 10 == 1:
    print("корова")

elif 1 < n % 10 <= 4:
    print("коровы")

else:
    print("коров")
