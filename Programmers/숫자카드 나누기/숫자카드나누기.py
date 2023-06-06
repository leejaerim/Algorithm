from math import gcd
# def calculate_gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
def find_common_divisors(numbers):
    gcd_num = numbers[0]
    for number in numbers:
        gcd_num = gcd(gcd_num, number) # calculate_gcd(gcd_num, number)
    common_divisors = find_divisors(gcd_num)
    return common_divisors

def find_divisors(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors
def isDivied(numbers:list,target:list):
    for i in target:
        temp = []
        for j in numbers:
            if i % j == 0:
                temp.append(j)
        for j in temp:
            numbers.remove(j)
    if len(numbers) == 0 :
        return [0]
    else:
        return numbers


def solution(array1:list, array2:list)->int:
    a = isDivied(find_common_divisors(array1),array2)
    b = isDivied(find_common_divisors(array2),array1)
    return max(max(a),max(b))