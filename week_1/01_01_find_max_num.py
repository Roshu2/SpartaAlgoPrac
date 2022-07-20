input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    for num in array:
        for compared_num in array:
            if num < compared_num:
                break
        else:
            return num

def find_max_num2(array):
    result = max(array)
    return result


result = find_max_num(input)
print(result)