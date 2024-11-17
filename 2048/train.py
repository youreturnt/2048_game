numbers = [1234,5678,9012]
target = 14690

array = []
for i, x in enumerate(numbers):
    find = target - x
    for j in numbers[:i]:
        if j == find:
            array.append(i)
            array.append(numbers.index(j))
result = tuple(array)
print(result[:2])