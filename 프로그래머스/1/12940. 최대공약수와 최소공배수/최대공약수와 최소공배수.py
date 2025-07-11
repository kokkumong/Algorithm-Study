def solution(n, m):
    answer = []
    #약수 찾기
    a = []
    for i in range(1,max(n,m)):
        if(n % i == 0 and m % i == 0):
            a.append(i)
    answer.append(max(a))
    #배수 찾기
    b = []
    for j in range(1,n*m + 1):
        if(j % n == 0 and j % m == 0):
            b.append(j)
    answer.append(min(b))
    #최소 공배수 찾기
    return(answer)