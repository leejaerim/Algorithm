def solution(elements:list)->int:
    memo = set()
    numberOfElements = len(elements)
    for length in range(1,numberOfElements+1):
        start = 0
        while start < numberOfElements:
            if start+length < numberOfElements :
                memo.add(sum(elements[start:(start+length)]))
            else :
                memo.add(sum(elements[start:]+elements[:(start+length)%numberOfElements]))
            start = start + 1
    return len(memo)