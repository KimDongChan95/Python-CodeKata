def solution(x):
    answer =  x%(sum(int(digit) for digit in str(x)))==0
    return answer

def solution(x):

solution이라는 이름의 함수를 정의합니다. x는 함수의 입력 매개변수로, 하샤드 수인지 판별할 정수를 받습니다.
answer = x % (sum(int(digit) for digit in str(x))) == 0

이 줄은 x가 하샤드 수인지 여부를 True 또는 False로 판별합니다.
str(x): x를 문자열로 변환하여 각 자리수를 개별적으로 다룰 수 있도록 합니다.
for digit in str(x): 문자열로 변환된 x의 각 자리수를 반복적으로 순회합니다.
int(digit): 문자열로 된 각 자리수를 정수형으로 변환합니다.
sum(int(digit) for digit in str(x)): 각 자리수를 정수형으로 변환한 후 합산하여 x의 자리수의 합을 계산합니다.
x % ... == 0: x를 앞에서 계산한 자리수의 합으로 나눈 나머지가 0이면 True, 아니면 False를 반환합니다.
이 값을 answer에 저장합니다.
return answer

answer 값을 반환하여 함수의 결과로 제공합니다. answer는 True 또는 False가 되며, x가 하샤드 수라면 True, 그렇지 않다면 False를 반환합니다.