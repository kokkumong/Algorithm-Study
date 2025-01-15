def solution(a, b):
    c = []
    if (a < b):
        for i in range(a,b+1):
            c.append(i)
            
    if (b < a):
        for i in range(b,a+1):
            c.append(i)
    if(a==b):
        c.append(a)
            
    answer = sum(c)
    return answer