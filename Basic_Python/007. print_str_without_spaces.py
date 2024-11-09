str1, str2 = input().strip().split(' ')
print(str1, end="")
print(str2)

str1, str2 = input().strip().split(' ')
print(str1+str2)

#'구분자'. join(리스트) : 리스트에 있는 요소 하나하나를 합쳐서 
# 하나의 문자열로 바꿔서 변환하고 합칠때, 구분자를 중간중간 넣어줍니다.

result = ''.join([str1, str2])
print(result)