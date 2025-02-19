def solution(phone_number):
    a = list(phone_number)
    for i in range(len(phone_number)-4):
        a[i] = "*"
    answer = ''.join(a)
    return answer
    