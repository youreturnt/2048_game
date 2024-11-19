import random
import pygame
import sys


def index_elem(num):  # от 1 до 16
    num = num - 1
    x, y = num//4, num % 4
    return x, y


def num_elem(a, b):
    return a * 4 + b + 1


def get_empty_list(mas):
    empty = []
    for i in range(4):
        for j in range(4):
            if mas[i][j] == 0:
                num = num_elem(i, j)
                empty.append(num)
    return empty


def insert_2_or_4(mas, x, y):
    if random.randint(0, 9) < 8:
        mas[x][y] = 2
    else:
        mas[x][y] = 4
    return mas

def different_nums(elem1):
    elem2 = random.randint(1, 16)
    if elem2 != elem1:
        return elem2
    return different_nums(elem1)


def mass_frontend(arr3):
    y = 30
    vert = 0
    for c0 in range(4):
        x = 30
        gor = 0
        for c1 in range(4):
            font = pygame.font.SysFont('couriernew', 60) #шрифт
            text = font.render(str(arr3[vert][gor]), True,(0, 0, 0))
            screen.blit(text, (x, y))
            x += 90
            gor += 1
        y += 60
        vert += 1


def mass_frontend1(arr3, turple):
    y = 30
    vert = 0
    for c0 in range(4):
        x = 30
        gor = 0
        for c1 in range(4):
            font = pygame.font.SysFont('couriernew', 60) #шрифт

            text = font.render(str(arr3[vert][gor]), True, (0, 0, 0))

            text2 = font.render(str(arr3[vert][gor]), True, (255, 255, 255))
            if c0 == turple[0] and c1 == turple[1]:
                screen.blit(text2, (x, y))
                x += 90
                gor += 1
            else:
                screen.blit(text, (x, y))
                x += 90
                gor += 1
        y += 60
        vert += 1


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
            point += row_list[i]
            row_list[i+1] = 0

    array.clear()
    for n in row_list:  # цифры влево, нули вправо
        if n > 0:
            array.append(n)
    array.extend([0] * row_list.count(0))
    return array


def move_right(array):
    global point
    row_lis = []
    row_lis.extend([0] * array.count(0))
    for num in reversed(array):
        if num > 0:
            row_lis.append(num)

    for i in range(len(row_lis)-1):  # суммирует соседние одинаковые цифры
        if row_lis[i] == row_lis[i+1]:
            row_lis[i] = (row_lis[i])*2
            point += row_lis[i]
            row_lis[i+1] = 0

    array.clear()
    array.extend([0] * row_lis.count(0))
    for n in reversed(row_lis):  # цифры влево, нули вправо
        if n > 0:
            array.append(n)
    return array


def flip_90_array(array):
    arr1 = []
    for i in list(zip(*array)):
        arr1.append(list(i))
    return arr1


arr = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

colors = {
    'background': (90, 90, 90),
    'empty_button': (130, 130, 120),
}

point = 0

n_elem = random.randint(1, 16)
n_elem2 = different_nums(n_elem)

insert_2_or_4(arr, index_elem(n_elem)[0], index_elem(n_elem)[1])
insert_2_or_4(arr, index_elem(n_elem2)[1], index_elem(n_elem2)[0])


pygame.init()
screen = pygame.display.set_mode((400, 500))
screen.fill(colors['background'])

mass_frontend(arr)

while point < 2048:
    arr_1 = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                for string in arr:
                    arr_1.append(move_left(string))
            elif event.key == pygame.K_RIGHT:
                for string in arr:
                    arr_1.append(move_right(string))
            elif event.key == pygame.K_UP:
                for string in flip_90_array(arr):
                    arr_1.append(move_left(string))
                arr_1 = flip_90_array(arr_1)
            elif event.key == pygame.K_DOWN:
                for string in flip_90_array(arr):
                    arr_1.append(move_right(string))
                arr_1 = flip_90_array(arr_1)

            print(point, 'point')

            spisok = len(get_empty_list(arr_1))
            number = random.randint(1, spisok)

            in_el = index_elem(get_empty_list(arr_1)[number - 1]) #свободные координаты
            #print(in_el)
            insert_2_or_4(arr_1, in_el[0], in_el[1]) # какое число разместить в массиве по свободным координатам

            arr = arr_1
            screen.fill(colors['background'])
            mass_frontend1(arr, in_el)

    pygame.display.flip()
