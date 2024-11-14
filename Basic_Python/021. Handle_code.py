def solution(code):
    ret = ""
    mode = 0  # 시작 모드는 0

    for idx in range(len(code)):
        if code[idx] == "1":  # "1"이 나타나면 모드 전환
            mode = 1 - mode
        else:
            if (mode == 0 and idx % 2 == 0) or (mode == 1 and idx % 2 != 0):
                ret += code[idx]

    return ret if ret else "EMPTY"
