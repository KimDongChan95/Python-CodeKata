def solution(x):
    answer =  x%(sum(int(digit) for digit in str(x)))==0
    return answer