def solution(n):
    for x in range(1, n + 1):
        if x * x == n:
            return (x + 1) * (x + 1)
        elif x * x > n:
            break
    return -1