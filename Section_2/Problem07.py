from collections import deque

Answer = deque()
BlockNum = int(input())

COUNT=1
for i in range(BlockNum):

        i=int(input())
        Answer.appendleft(i)
        
print(Answer)
n=Answer[0]
for j in range(len(Answer)-1):
        if Answer[j+1] > n:
                n=Answer[j+1]
                print(COUNT,Answer[j])
                COUNT=COUNT+1

print(COUNT)
