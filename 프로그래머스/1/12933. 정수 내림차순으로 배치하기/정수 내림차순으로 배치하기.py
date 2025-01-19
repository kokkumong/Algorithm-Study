def solution(n):
    a = list(str(n))
    a.sort(reverse = True)
    answer = int(''.join(map(str,a)))
    return answer