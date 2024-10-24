#정수 n이 주어졌을 때
#1부터 n 까지 순회하며 나눴을때 나머지가 0인 숫자들만 출력하기 

def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i==0:
            answer +=i
    return answer

print(solution(12))