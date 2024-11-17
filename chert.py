while point < 2048:
    count = input()
    #os.system('cls||clear')
    arr_1 = []
    if str(count) == 'a':
        for string in arr:
            arr_1.append(move_left(string))
    elif str(count) == 'd':
        for string in arr:
            arr_1.append(move_right(string))
    elif str(count) == 'w':
        for string in flip_90_array(arr):
            arr_1.append(move_left(string))
        arr_1 = flip_90_array(arr_1)
    elif str(count) == 's':
        for string in flip_90_array(arr):
            arr_1.append(move_right(string))
        arr_1 = flip_90_array(arr_1)

    print(point, ' point')

    spisok = len(get_empty_list(arr_1))
    number = random.randint(1, spisok)

    in_el = index_elem(get_empty_list(arr_1)[number - 1])
    insert_2_or_4(arr_1, in_el[0], in_el[1])

    arr = arr_1
    out_mas(arr_1)