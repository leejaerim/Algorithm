###

#- bin, oct, hex 와같이 2진,8진, 16진수로 표현할 수 있다.
#    - 단 0x,0o,0h와 같은 접두어가 붙는것에 유의해야합니다.
#- `format(42, 'b')`  와 같이 표현할 수 도 있음.
###
def solution(s:str)->list:
    total = 0
    cnt = 0
    while s != "1":
        cnt += s.count("0")
        c = len(s.replace("0",''))
        s = bin(c)[2:]
        total += 1
    return [total, cnt]