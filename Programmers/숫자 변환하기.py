from collections import deque


def solution(x, y, n):
    visited = [False] * (y + 1)
    queue = deque([(x, 0)])
    visited[x] = True

    while queue:
        num, cnt = queue.popleft()
        if num == y:
            return cnt
        if num + n <= y and not visited[num + n]:
            visited[num + n] = True
            queue.append((num + n, cnt + 1))
        if num * 2 <= y and not visited[num * 2]:
            visited[num * 2] = True
            queue.append((num * 2, cnt + 1))
        if num * 3 <= y and not visited[num * 3]:
            visited[num * 3] = True
            queue.append((num * 3, cnt + 1))

    return -1기