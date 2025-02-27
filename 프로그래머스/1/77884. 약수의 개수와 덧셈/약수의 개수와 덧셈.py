def solution(left, right):
    a = []
    b = []
    c = []
    for i in range(left,right+1):
        for j in range(1,i+1): 
            if (i % j == 0):
                a.append(j)
        if(len(a) % 2 == 0):
            b.append(i)
        else:
            c.append(i)
        del a[:]
    return sum(b) - sum(c) 
