def solution(n):
    answer = []
    a = list(str(n))
    a.reverse()
    for i in range(len(a)):
        answer.append(int(a[i]))
    
    return answer