from collections import defaultdict

def solution(nums):
    answer=-1
    dic = defaultdict(int);     # int 를 붙히는건 디폴트밸류 타입을 선언 하는거임

    for key in nums:            # 중복된 수를 체크한다
        if key in dic:
             dic[key] = 1         

    for x in dic:               # 가장 큰 값을 찾는다.
        if dic[x] == 1 :
            answer=max(x, answer)


    return answer

print(solution([3,9,2,12,9,12,8,7,9,12]))
print(solution([2,1,3,2,1,3,4,5,4,5,6,7,6,7,8,8]))
print(solution([23, 56, 11, 67, 120, 560, 812, 960, 560, 777, 888, 960] ))
print(solution([2235253, 5525612, 142561567, 123456789, 2235253,560, 123456789, 142561567]))