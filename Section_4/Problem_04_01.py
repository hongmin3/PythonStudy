def solution(nums):
    answer = 0
    flag = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(len(nums)):
        for j in range(len(nums)):
            # flag = 0
            flag = True
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
            #     if nx < 0 or nx > 4 or ny < 0 or ny > 4:      # 웅덩이인지 찾는 로직
            #         flag +=1                                  # 가장자리 1000지점을 찾는 로직

            #     if nx >= 0 and nx < 5 and ny >= 0 and ny < 5:  # 4면이 가운데보다 작은지 확인하는 로직
            #         if nums[nx][ny] > nums[i][j]:
            #             flag += 1
            # if flag == 4:
            #     answer+=1
                
            # lecture answer
                if nx >= 0 and nx < 5 and ny >= 0 and ny < 5 and nums[i][j] >= nums[nx][ny]:
                    flag=False
                    break
            if  flag==True:
                 answer+=1
                
    return answer
         
print(solution([[10, 20, 50, 30, 20], [20, 30, 50, 70, 90], [10, 15, 25, 80, 35], [25, 35, 40, 55, 80], [30, 20, 35, 40, 90]]))
print(solution([[80, 25, 10, 65, 100], [20, 10, 32, 70, 33], [45, 10, 88, 9, 90], [10, 35, 10, 55, 66], [10, 84, 65, 88, 99]]))
print(solution([[33, 22, 55, 65, 55], [55, 88, 99, 12, 19], [18, 33, 25, 57, 77], [46, 78, 54, 55, 99], [33, 25, 47, 85, 17]]))
