def solution(moves):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dir = ['G', 'R', 'L']
    for c in moves:
        for k in range(4):
            if c == dir[k]:
                x = x + dx[k]
                y = y + dy[k]
         
    return [x, y]
                            
print(solution('GGGRGGG'))
print(solution('GGRGGG'))
print(solution('GGGGGGGRGGGRGGRGGGLGGG'))
print(solution('GGLLLGLGGG'))
