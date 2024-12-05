def solution(n):
        answer = 0
        for x in list(str(n)):
            answer += int(x)
        
        return answer

print(solution(4583))


def solution(N):
    return sum(int(x) for x in str(N))

print(solution(1263))  # 출력: 12