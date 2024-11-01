def solution(n): #solution함수 정의 
   for x in range(1, n + 1):
        if x * x == n:
            return (x + 1) * (x + 1)
        elif x * x > n:
            return -1 