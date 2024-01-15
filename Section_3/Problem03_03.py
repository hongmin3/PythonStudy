from collections import defaultdict
from collections import Counter

def solution(nums):
    # answer=1000000
    # dic = defaultdict(int);
    # for key in nums:
    #     if key in nums:
    #          dic[key] += 1

    # print(dic)
    # for x in dic:
    #     if dic[x] == x :
    #         answer=min(x, answer)
    
    # if answer == 1000000:
    #     answer=-1

    answer=1000000
    nH = Counter(nums)   # 원소의 개수를 카운팅 할 수 있는 함수
    for key in nH:
        if nH[key] == key :  # 자기 분열 수를 찾기
            answer = min(answer,key) 

    return -1  if answer == 1000000 else answer    # 자기 분열 수가 없는 입력값이 들어왔을 때 예외처리

print(solution([1, 2, 3, 1, 3, 3, 2, 4]))
print(solution([1, 2, 3, 3, 3, 2, 4, 5, 5, 5] ))
print(solution([1, 1, 2, 5, 5, 5, 5, 5, 3, 3, 3, 3, 5] ))
print(solution([2235253, 5525612, 142561567, 123456789, 2235253,560, 123456789, 142561567]))