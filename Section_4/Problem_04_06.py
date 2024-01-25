
def solution(x, y, d, board):  
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    direction = [3, 0, 1, 2]
    board[x][y] = 2  #청소한 칸은 2로 변경한다.
    answer = 1
    flag=0
  
    while(1):
        if board[x][y] != 2:
            board[x][y] = 2    #1번 경우의수
            answer +=1
        for i in range(4):
            if board[x+dx[i]][y+dy[i]] == 1:
                flag +=1

        if flag == 4 :         
            x = x - dx[direction.index(d)]
            x = y - dy[direction.index(d)]
            if board[x][y] == 1 and x < 0 or x > 11 or y < 0 or y > 10:
                return answer
            break
        else:
            d = direction.index(d) + 1
            if d == 4:
                d = 0
            x = x + dx[direction.index(d)]
            y = y + dy[direction.index(d)]           

        print(answer)
    return answer
   

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
print(solution(r, c, d, arr))