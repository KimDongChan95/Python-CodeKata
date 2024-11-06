def solution(n):
    answer = [int(i) for i in str(n)[::-1]]
    return answer

# 예시
n = 13846
print(solution(n))  
