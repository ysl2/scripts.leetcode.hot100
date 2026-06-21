from collections import Counter

def main(s, p):
    window = Counter(p)
    res = []
    left = 0
    for right in range(len(s)):
        window[s[right]] -= 1
        while window[s[right]] < 0:
            window[s[left]] += 1
            left += 1
        if right - left + 1 == len(p):
            res.append(left)
    return res

s = "cbaebabacd"
p = "abc"
print(main(s, p))