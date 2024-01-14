def solution(nums):
    answer=-1
    cnt = [0] * 1001
    for x in nums:
        cnt[x] += 1

    for i in range(1,1001):
        if cnt[i] == 1:
            answer = max(answer, i)

   
    return answer

print(solution([3,9,2,12,9,12,8,7,9,12]))