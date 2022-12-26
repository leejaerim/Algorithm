def solution(n, words):
    answer = []
    is_called = []
    count = 0
    user_count = {}
    prev = ""
    for word in words:
        if word in is_called:
            return [count%n + 1,count//n+1]
        else:
            if prev != "" and prev != word[:1]:
                return [count%n + 1,count//n+1]
            prev = word[-1:]
            is_called.append(word)
        count += 1
    return [0,0]