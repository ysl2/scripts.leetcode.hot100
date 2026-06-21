from collections import defaultdict

def main(strs):
    mp = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        mp[key].append(s)
    return list(mp.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(main(strs))