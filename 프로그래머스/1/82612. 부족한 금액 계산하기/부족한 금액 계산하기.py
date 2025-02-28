def solution(price, money, count):
    total_fee = 0
    for i in range(1,count + 1):
        total_fee += price * i
        
    if (total_fee > money):
        return total_fee - money
    else:
        return 0