def solution(a, b):
    if int(str(a) + str(b)) > 2 * a * b:
        return int(str(a) + str(b))
    elif 2 * a * b > int(str(a) + str(b)):
        return 2 * a * b
    else:
        return int(str(a) + str(b))
