from collections import Counter

def main(s, t):
    cnt = Counter(t)
    less = len(cnt)
    ml, mr = -1, len(s)
    left = 0
    for right in range(len(s)):
        cnt[s[right]] -= 1
        if cnt[s[right]] == 0:
            less -= 1
        while less == 0:
            if right - left < mr - ml:
                ml, mr = left, right
            if cnt[s[left]] == 0:
                less += 1
            cnt[s[left]] += 1
            left += 1
    return s[ml : mr + 1] if ml != -1 else ''

s = "ADOBECODEBANC"
t = "ABC"
print(main(s, t))