input = "abcba"

#회문 재귀함수 활용
#문제가 축소되며 반복되는것 같으면, 재귀함수로 풀어 볼 수 있다는 추측을 할 수 있게 된다.
#재귀함수를 풀때는 탈출조건을 작성해야한다.
def is_palindrome(string):
    if len(string) <= 1:
        return True

    if string[0] != string[-1]:
        return False

    return is_palindrome(string[1:-1])


print(is_palindrome(input))