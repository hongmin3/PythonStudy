def solution(nums):
    answer=0
    temp=0

    for i in nums:
        if i == 1:
           temp+=1
           if temp >= answer:
               answer=temp
        else:
            temp=0
        

    return answer

print(solution([1,1,0,1,1,1,0,1,1,1,1,1]))
print(solution([0,0,1,0,1,0,0]))
print(solution([1,1,1,1,1]))
print(solution([1,0,1,1,0,1,1,1,0,1,1,1,0,1]))