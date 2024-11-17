import time


def out_mas(mas):   # вывод двумерного массива
    for rows in mas:
        print(*rows)



def my_random(n):
    if len(str(n)) == 1:
        return n
    int_list = []
    for i in str(n):
        int_list.append(int(i))
    n = sum(int_list)
    return my_random(n)


def random_1_to_16(n):
    num = int(n[0]) + int(n[1])
    if num > 16:
        return 1
    return num


def num_elem(a, b):
    return a * 4 + b + 1


def index_elem(num):  # от 1 до 16
    num = num - 1
    x, y = num//4, num % 4
    return x, y


def get_empty_list(mas):
    empty = []
    for i in range(4):
        for j in range(4):
            if mas[i][j] == 0:
                num = num_elem(i, j)
                empty.append(num)
    return empty


def insert_2_or_4(mas, x, y):
    if my_random(str(time.time())[-3:]) < 7:
        mas[x][y] = 2
    else:
        mas[x][y] = 4
    return mas


def move_left(array):
    global point
    row_list = []  # цифры влево, нули вправо
    for num in array:
        if num > 0:
            row_list.append(num)
    row_list.extend([0]*array.count(0))

    for i in range(len(row_list)-1):  # суммирует соседние одинаковые цифры
        if row_list[i] == row_list[i+1]:
            row_list[i] = (row_list[i])*2
            point += (row_list[i])*2
            row_list[i+1] = 0

    array.clear()
    for n in row_list:  # цифры влево, нули вправо
        if n > 0:
            array.append(n)
    array.extend([0] * row_list.count(0))

    return array


def move_right(array):

    row_lis = []
    row_lis.extend([0] * array.count(0))
    for num in reversed(array):
        if num > 0:
            row_lis.append(num)

    for i in range(len(row_lis)-1):  # суммирует соседние одинаковые цифры
        if row_lis[i] == row_lis[i+1]:
            row_lis[i] = (row_lis[i])*2
            point += (row_lis[i]) * 2
            row_lis[i+1] = 0

    array.clear()
    array.extend([0] * row_lis.count(0))
    for n in reversed(row_lis):  # цифры влево, нули вправо
        if n > 0:
            array.append(n)
    return array


def flip_90_array(array):
    arr_1 = []
    for i in list(zip(*array)):
        arr_1.append(list(i))
    array = arr_1
    return array


def move_up(array):
    arr_1 = []
    for i in flip_90_array(array):
        arr_1.append(move_left(i))
    return flip_90_array(arr_1)
