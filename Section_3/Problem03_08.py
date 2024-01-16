from collections import defaultdict, Counter
def solution(participant, completion):
    answer = ''

    nH=defaultdict(int)

    for key in participant: 
        if key in participant:
             nH[key] += 1         #동명이인이 있을 수 있는걸 감안하여 key를 사람이름으로 하고 
                                   #value를 해당 사람의 명수로 하는 딕셔너리 생성
    
    for str in completion:        #완주자 명단을  key와 비교하여 value를 하나씩 뺴기
        if str in nH:
            nH[str] -= 1

    for key, val in nH.items():    #입력이 문제가 없었을 경우 딕셔너리의 value가 1개인 key는 하나밖에 없을테니 그걸출력
        if val == 1:
            answer=key
    return answer


n = int(input())
a = []
for i in range(n):
    a.append(input())
b = []
for i in range(n-1):
    b.append(input())
print(solution(a, b))