def solution(x):
    a = list(str(x))
    total = 0
    for i in a:
        total += int(i)
        
    if(x % total == 0):
        return True
    else:
        return False
    