def solution(s):
    num = int(len(s)/2)
    if (len(s) % 2 != 0):
        answer = s[num]
    else:
        answer = s[num - 1] + s[num]
    return answer