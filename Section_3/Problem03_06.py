from collections import defaultdict, Counter
def solution(nums,target):
    answer=[0,0]

    nH=defaultdict(int)

    for key in nums:
        y = target - key
        if y in nH:
             return sorted([y, key])
        else :
            nH[key]=1 


    return answer     

print(solution([7,3,2,13,9,15,8,11],12))
print(solution([21,12,30,15,6,2,9,19,14],24))
print(solution([12,18,5,8,21,27,22,25,16,2],28))
print(solution([11,17,6,8,21,9,19,12,25,16,2],26))
print(solution([7,5,12,-9,-12,22,-30,-35,-21],-14))
print(solution([7,5,12,20],15))