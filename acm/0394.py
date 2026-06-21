def main(s):
    st, res, num = [], '', 0
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c == '[':
            st.append((res, num))
            res, num = '', 0
        elif c == ']':
            tmp = st.pop()
            res = tmp[0] + tmp[1] * res
        else:
            res += c
    return res


s = "3[a]2[bc]"
print(main(s))

s = "3[a2[c]]"
print(main(s))

s = "2[abc]3[cd]ef"
print(main(s))

s = "abc3[cd]xyz"
print(main(s))