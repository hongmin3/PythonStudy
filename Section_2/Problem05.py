from collections import deque
def solution(nums):
#    Answer= list(set(nums))
#    Answer.sort(reverse=True) 
    Answer = deque()
    Answer.appendleft(nums[0])
    for i in range(1,len(nums)):
        if nums[i] != Answer[0]:
            Answer.appendleft(nums[i])
        
    return Answer


print(solution([0,1,1,1,2,2,2,3]))
print(solution([1,1,2,2,2,3,3,3,3,3,4,4,4,5]))
print(solution([0,0,0,3,3,3,5,7,7,7]))
print(solution([1,2,3,4,5,6,7,7,7,8,9]))