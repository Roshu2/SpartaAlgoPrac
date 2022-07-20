input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    if number in array:
        return True
    return False


def is_number_exist2(number, array):
    for element in array:
        if number == element:
            return True
        return False

#빅오 표기법 알고리즘의 가장 성능이 최악일 경우를 생각하여 분석을 한다.
result = is_number_exist(3, input)
print(result)