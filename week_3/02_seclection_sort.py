input = [4, 6, 2, 9, 1, 3, 12, 11, 5]

#선택정렬
def selection_sort(array):
    n = len(array) #O(N^2) 시간복잡도 반복문 2번이기때문

    for i in range(n - 1):
        min_index = i
        for j in range(n - i):
            if array[i + j] < array[min_index]:
                min_index = i + j
        array[i], array[min_index] = array[min_index], array[i]
    return


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!