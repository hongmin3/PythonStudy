def solution(weight, limit):
    answer=0
    Allweight=0
    n = len(weight)
    weight.sort()

    for i in range(n):
        Allweight+=weight[i]
        if Allweight < limit:
            answer+=1

    return answer
         
print(solution([300, 100, 230, 120, 90, 150, 60], 700 ))
print(solution([50, 90, 70, 120, 300, 200, 150, 180, 190], 1000 ))
print(solution([70, 90, 100, 80, 60, 75, 73, 85, 120, 110, 200] ,800 ))
print(solution([50, 90, 100, 130, 140, 120, 130, 120, 150, 160, 140,170], 1000))
print(solution([100, 110, 50, 50, 60, 70, 50, 55, 57] ,350))
