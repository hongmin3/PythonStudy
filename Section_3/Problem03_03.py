def solution(nums):
    answer=-1
    cnt=[]
    dic = dict();
    for key in nums:
        if key not in dic:
             dic[key] = 1
        else:
            dic[key] += 1

    for x in dic:
        if dic[x] == x :
            cnt.append(x)

    if len(cnt) != 0: 
        answer=min(cnt)


    return answer

print(solution([1, 2, 3, 1, 3, 3, 2, 4]))
print(solution([1, 2, 3, 3, 3, 2, 4, 5, 5, 5] ))
print(solution([1, 1, 2, 5, 5, 5, 5, 5, 3, 3, 3, 3, 5] ))
#print(solution([2235253, 5525612, 142561567, 123456789, 2235253,560, 123456789, 142561567]))