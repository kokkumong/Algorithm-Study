def solution(absolutes, signs):
    for i in range(len(absolutes)):
        if (signs[i] == False):
            absolutes[i] = 0 - absolutes[i]
    return sum(absolutes)
    answer = 123456789
    return answer