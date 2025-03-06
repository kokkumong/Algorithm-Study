def solution(n, m):
    answer = []
    #약수 찾기
    a = []
    b = []
    for i in range(1,n+1):
        if(n % i == 0):
            a.append(i)
    for j in range(1,m+1):
        if(m % j == 0):
            b.append(j)
    #최대공약수 구하기
    GCD = max(set(a) & set(b))
    answer.append(GCD)
    #배수 찾기
    d = []
    e = []
    for i in range(1,m + 1):
        d.append(n*i)
    for j in range(1,n+1):
        e.append(m*j)
    #최소 공배수 찾기
    LCD = min(set(d) & set(e))
    answer.append(LCD)
    return answer