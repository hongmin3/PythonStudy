def solution(moves):

    nx = ny = 0

    for i in moves:
        if i == 'U':
            nx -= 1
        elif i == "R" :
            ny += 1
        elif i == "L" :
            ny -= 1
        elif i == 'D' :
            nx += 1
    
        if nx < 0 :
            nx = 0
        if ny < 0 :
            ny = 0
        answer = [nx, ny]

    return answer
         
print(solution('RRRDDDLU'))
print(solution('DDDRRRDDLL'))
print(solution('RRRRRRDDDDDDUULLL'))
print(solution('RRRRDDDRRDDLLUU'))

