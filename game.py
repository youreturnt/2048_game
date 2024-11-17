import random
import pygame
import sys
from logics import index_elem, get_empty_list, insert_2_or_4, flip_90_array


def mass_frontend(arr3):
    y = 30
    vert = 0
    for j in range(4):
        x = 30
        gor = 0
        for i in range(4):
            font = pygame.font.SysFont('couriernew', 60)
            text = font.render(str(arr3[vert][gor]), True, colors['full_button'])
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


arr = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

colors = {
    'background': (90, 90, 90),
    'empty_button': (130, 130, 120),
    'full_button': (0, 0, 0)
}

point = 0

n_elem = random.randint(1, 16)
n_elem_2 = random.randint(1, 16)
if n_elem_2 == n_elem:
    n_elem_2 = random.randint(1, 16)


insert_2_or_4(arr, index_elem(n_elem)[0], index_elem(n_elem)[1])
insert_2_or_4(arr, index_elem(n_elem_2)[1], index_elem(n_elem_2)[0])


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

            in_el = index_elem(get_empty_list(arr_1)[number - 1])
            insert_2_or_4(arr_1, in_el[0], in_el[1])

            arr = arr_1
            screen.fill(colors['background'])
            mass_frontend(arr)
    pygame.display.flip()
