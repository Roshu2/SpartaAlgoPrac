input = 20
#
# #소수는 자기 자신과 1외에는 아무것도 나눌 수 없다.
# #주어진 자연수 N이 소수이기 위한 필요 충분 조건은 N이 N의
# def find_prime_list_under_number(number):
#     prime_number_list = []
#     prime_number = 0
#     for i in range(number):
#         prime_number = prime_number + i
#         if prime_number % prime_number == 0 and prime_number % 1 == 0:
#             return prime_number_list.append(prime_number)
#
#
# result = find_prime_list_under_number(input)
# print(result)

# def find_prime_list_under_number(number):
#     prime_list = []
#     for n in range(2, number + 1): # n의 범위 <- 2 ~ number
#         for i in range(2, n): # i 의 범위 : 2부터 n -1 까지
#             if n % i == 0:
#                 break
#         else:
#             prime_list.append(n)
#
#     return prime_list
#
# 개선 1
# def find_prime_list_under_number(number):
#     prime_list = []
#     for n in range(2, number + 1): # n의 범위 <- 2 ~ number
#         for i in prime_list: # i 의 범위 : prime_list 즉 소수가지고만.
#             if n % i == 0:
#                 break
#         else:
#             prime_list.append(n)
#
#     return prime_list


# result = find_prime_list_under_number(input)
# print(result)

# 개선 2
def find_prime_list_under_number(number):
    prime_list = []
    for n in range(2, number + 1): # n의 범위 <- 2 ~ number
        for i in prime_list: # i 의 범위 : prime_list 즉 소수가지고만.
            if n % i == 0 and i * i <= n: #i 중에서도 소수 조건에 나눠볼 필요가 있는 숫자만
                break
        else:
            prime_list.append(n)

    return prime_list


result = find_prime_list_under_number(input)
print(result)



