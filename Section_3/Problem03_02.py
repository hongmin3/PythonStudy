def solution(nums):
    answer=-1
    dic = dict();
    for key in nums:
        if key not in dic:
             dic[key] = 1
        else:
            dic[key] += 1

    for x in dic:
        if dic[x] == 1 :
            answer=max(x, answer)


    return answer

print(solution([3,9,2,12,9,12,8,7,9,12]))
print(solution([2,1,3,2,1,3,4,5,4,5,6,7,6,7,8,8]))
print(solution([23, 56, 11, 67, 120, 560, 812, 960, 560, 777, 888, 960] ))
print(solution([2235253, 5525612, 142561567, 123456789, 2235253,560, 123456789, 142561567]))