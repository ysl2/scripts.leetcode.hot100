def main(s):
    stack = []
    mp = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in '([{':
            stack.append(c)
        elif not stack or stack[-1] != mp[c]:
            return False
        else:
            stack.pop()
    return not stack


s = "()"
print(main(s))

s = "()[]{}"
print(main(s))

s = "(]"
print(main(s))

s = "([])"
print(main(s))

s = "([)]"
print(main(s))