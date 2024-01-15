from collections import defaultdict
from collections import Counter

def solution(s):
#   answer=False
    cnt=0
    nH=Counter(s)             # 스트링에 알파벳 빈도수 찾기

    for key in nH:
        if nH[key] % 2 == 1:  
            cnt+=1            # 홀수개인 알파벳 카운트

#    if cnt == 1 or cnt == 0:
#        answer=True           # 홀수개인 알파벳이 아예없거나 1개만 있는 경우는 펠린드롬이 가능

    return cnt <= 1     # 홀수개인 알파벳이 1보다 작으면 팰린드롬이 가능하니 이렇게 리턴문을 짜면 더 간편하다

print(solution("abacbaa" ))
print(solution("abaaceeffkckbaa"))
print(solution("abcabbcc" ))
print(solution("sgsgsgabaaaecececekefefkccckbsgaaffsgsg" ))
print(solution("aabcefagcefbcabbcc"))