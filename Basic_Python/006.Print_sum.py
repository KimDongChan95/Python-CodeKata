a, b = map(int, input().strip().split(' '))
print(str(a) + " + " + str(b) + " = " + str(a+b))

a, b = map(int, input().strip().split(' '))
print(f"{a} + {b} = {a+b}")

# f-string은 가독성이 높습니다. 변수나 표현식을 직접 중괄호 {} 안에 넣어 쉽게 작성할 수 있습니다.
# str()은 문자열을 연결할 때 사용되며, 여러 변수나 표현식을 결합해야 할 때 코드가 길어지고 복잡해질 수 있습니다.