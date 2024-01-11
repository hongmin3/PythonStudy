def solution(nums):
    answer=0
    dic = dict()
    for key in nums:
        if key not in dic:
            dic[key] = 1
        else:
            dic[key] += 1

    for key in nums:
        if dic(key) =! 1:
            del dic(key)

    for key in 

   
    return answer

print(solution([3,9,2,12,9,12,8,7,9,12]))