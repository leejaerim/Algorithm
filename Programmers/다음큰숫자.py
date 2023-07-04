# from collections import Counter
# def solution(n:int)->int:
#     cnt = Counter(bin(n).replace('0b',''))
#     target = cnt['1']
#     while True:
#         n+=1
#         cnt = Counter(bin(n).replace('0b',''))
#         if target == cnt['1']:
#             return n

def solution(n:int)->int:
    target = bin(n).count('1')
    while True:
        n+=1
        cnt = bin(n).count('1')
        if target == cnt:
            return n