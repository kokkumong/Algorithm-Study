def solution(n):
    a = []
    
    for i in range(1,n):
        if(n > i):
            if(n % i == 1):
                a.append(i)
                answer = a[0]
    return answer