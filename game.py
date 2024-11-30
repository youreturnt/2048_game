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


def mass_frontend(arr3, turple):
    y = 30
    vert = 0
    for c0 in range(4):
        x = 50
        gor = 0
        for c1 in range(4):
            fonts = pygame.font.SysFont('Terminal', 60) #шрифт
            font2 = pygame.font.SysFont('Terminal', 50)  #шрифт для трехзначного числа


            text = fonts.render(str(arr3[vert][gor]), True, (0, 0, 0))
            text2 = fonts.render(str(arr3[vert][gor]), True, (255, 255, 255)) # для нового числа
            text3 = font2.render(str(arr3[vert][gor]), True, (0, 0, 0))

            if c0 == turple[0] and c1 == turple[1]:
                screen.blit(text2, (x, y))
                x += 90
                gor += 1
            elif len(str(arr3[c0][c1])) == 2:
                screen.blit(text, (x-15, y))
                x += 90
                gor += 1
            elif len(str(arr3[c0][c1])) == 3:
                screen.blit(text3, (x-20, y))
                x += 90
                gor += 1
            else:
                screen.blit(text, (x, y))
                x += 90
                gor += 1
        y += 60
        vert += 1


def end_game():

    you_dead_font = pygame.font.SysFont('Terminal', 80)  # шрифт
    you_dead = you_dead_font.render('End Game', True, (255, 0, 0))

    screen.fill(colors['background'])
    screen.blit(you_dead, (60, 150))



def move_left(array):
    global point
    array.sort(key=lambda x: x == 0)  # цифры влево, нули вправо

    for i in range(len(array)-1):  # суммирует соседние одинаковые цифры
        if array[i] == array[i+1]:
            array[i] = (array[i])*2
            point += array[i]
            array[i+1] = 0

    array.sort(key=lambda x: x == 0) # цифры влево, нули вправо
    return array


def move_right(array):
    global point
    array.sort(key=lambda x: x != 0)  # цифры вправо, нули влево

    for i in reversed (range(len(array)-1)):  # суммирует соседние одинаковые цифры
        if array[i] == array[i + 1]:
            array[i] = (array[i]) * 2
            point += array[i]
            array[i + 1] = 0

    array.sort(key=lambda x: x != 0) # цифры вправо, нули влево
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

print(n_elem, n_elem2)

insert_2_or_4(arr, index_elem(n_elem)[0], index_elem(n_elem)[1])
insert_2_or_4(arr, index_elem(n_elem2)[1], index_elem(n_elem2)[0])

pygame.init()
screen = pygame.display.set_mode((400, 500))
screen.fill(colors['background'])

mass_frontend(arr, (10,10) ) #выводит массив в окно

font = pygame.font.SysFont('Terminal', 60) #шрифт
text_score = font.render('score: ', True, (0, 0, 0))


while point < 30000:
    screen.blit(text_score, (50, 350))
    for event in pygame.event.get():
        arr_1 = []
        text_point = font.render(str(point), True, (0, 0, 0))

        screen.blit(text_point, (250, 350))

        if event.type == pygame.QUIT: #Если одно из событий соответствует сигналу к завершению программы, закрываем окно.
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
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

            spisok = len(get_empty_list(arr_1)) #количество нулей (свободных мест) в массиве
            if spisok == 0:
                end_game()
                break

            else:
                number = random.randint(1, spisok) #

                in_el = index_elem(get_empty_list(arr_1)[number - 1]) #свободные координаты
                insert_2_or_4(arr_1, in_el[0], in_el[1]) # какое число разместить в массиве по свободным координатам

                arr = arr_1
                screen.fill(colors['background'])

                mass_frontend(arr_1, in_el) #массив с новым числом

        pygame.display.flip()
