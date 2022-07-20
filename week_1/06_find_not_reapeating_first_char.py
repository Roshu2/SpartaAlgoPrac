input = "abadabac"

def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26
    for char in string:
        if not char.isalpha():
            continue #반복문의 다음 인덱스로 넘어가게하는 방법
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1
        print(alphabet_occurrence_array)
        for i in alphabet_occurrence_array:
            if i == 0:
                return chr(i + ord("a"))
            else:
                return "_"


result = find_not_repeating_character(input)
print(result)