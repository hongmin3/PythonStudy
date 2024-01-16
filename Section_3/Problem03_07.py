from collections import defaultdict, Counter
def solution(n, m, name):
    answer=[]

    nH=Counter(name)

    for key, val in nH.items():
        if val == 2:
            answer.append(key)

    print(len(answer))
    for i in sorted(answer):
        print (i, sep='\n')
        return 0

arr = []
n, m = map(int, input().split())
for i in range(n+m):
    arr.append(input())

solution(n, m, arr)