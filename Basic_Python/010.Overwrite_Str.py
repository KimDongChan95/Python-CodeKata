def solution(my_string, overwrite_string, s):
    # my_string을 리스트로 변환
    my_string_list = list(my_string)
    
    # 주어진 위치 s부터 overwrite_string의 길이만큼 덮어쓰기
    my_string_list[s:s + len(overwrite_string)] = list(overwrite_string)
    
    # 리스트를 문자열로 결합하여 반환
    answer = ''.join(my_string_list)
    return answer

print(solution("He11oWor1d", "lloWorl", 2))

