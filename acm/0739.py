def main(ts):
    st = []
    res = [0] * len(ts)
    for i in range(len(ts)):
        while st and ts[st[-1]] < ts[i]:
            j = st.pop()
            res[j] = i - j
        st.append(i)
    return res


temperatures = [73,74,75,71,69,72,76,73]
print(main(temperatures))