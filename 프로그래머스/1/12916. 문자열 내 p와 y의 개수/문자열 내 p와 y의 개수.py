def solution(s):
    a = s.count('p') + s.count('P')
    b = s.count('y') + s.count('Y')
    if(a == b):
        return True
    else:
        return False
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')