from collections import defaultdict
from collections import Counter

def solution(s):
    answer=0
    cnt=0
    nH=Counter(s)             # 스트링에 알파벳 빈도수 찾기

    for key in nH:
        if nH[key] % 2 == 1:  
            cnt+=1            # 홀수개인 알파벳 카운트
        answer=len(s)

    if cnt > 1:
        answer=answer-cnt+1           # 홀수개가 2개 이상이라 모든 스트링이 펠린드롬이 안될경우, 최대한 펠린드롬이 될 수 있는 길이를 구한다


    return answer     

print(solution("abcbbbccaaeee" ))
print(solution("aabbccddee"))
print(solution("fgfgabtetaaaetytceefcecekefefkccckbsgaafffg"  ))
print(solution("aabcefagcefbcabbcc" ))
print(solution("abcbbbccaa" ))