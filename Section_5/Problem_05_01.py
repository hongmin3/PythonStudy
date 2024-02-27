def solution(nums):
    answer = 0
    nums.sort

    arr = []
    for value in nums:
        if value not in arr:
            arr.append(value)

    if len(nums) / 2 >= len(arr) :
        return len(arr)
    else:
        return len(arr) // 2 
         
print(solution([2, 1, 1, 3, 2, 3, 1, 2] ))
print(solution([1, 3, 5, 7, 2, 3, 7, 5, 3, 2, 5, 7, 9, 12] ))
print(solution([5, 5, 5, 5, 5, 5] ))
print(solution([12, 23, 11, 3, 5, 23, 23, 23, 23, 23, 23, 23]  ))
print(solution([100, 200, 300, 400, 500, 600, 700, 800] ))
