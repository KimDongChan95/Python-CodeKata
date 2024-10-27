def solution(n):
    return [int(digit) for digit in str(n)[::-1]]

# 예시
n = 13846
print(solution(n))  
