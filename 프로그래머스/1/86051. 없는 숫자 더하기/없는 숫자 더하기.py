def solution(numbers):
    a = [1,2,3,4,5,6,7,8,9,0]
    b = list(set(a) - set(numbers))
    return sum(b)