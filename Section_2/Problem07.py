from collections import deque

Answer = deque()
BlockNum = int(input())

COUNT=1
for i in range(BlockNum):

        i=int(input())
        Answer.appendleft(i)
        
print(Answer)

for j in range(len(Answer)-1):
        if  Answer[0] <= Answer[j+1]:
                COUNT=COUNT
        elif Answer[j+1] > Answer[j]:
                print(COUNT,Answer[j])
                COUNT=COUNT+1

print(COUNT)