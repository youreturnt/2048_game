import time


def digital_root(n):
    if len(str(n)) == 1:
        return n
    int_list = []
    for i in str(n):
        int_list.append(int(i))
    n = sum(int_list)
    return digital_root(n)

seed = str(time.time())[-3:]

print(digital_root(seed))

