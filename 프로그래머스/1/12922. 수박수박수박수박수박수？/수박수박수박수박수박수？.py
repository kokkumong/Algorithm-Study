def solution(n):
    answer = "수박"
    if(n >= 1):
        if(n % 2 == 0):
            answer = "수박" * (n//2)
            return answer 
        else:
            answer = "수박" * (n//2) + answer[0]          
            return answer 