def main(heights):
    st = []
    res = 0
    heights = [0] + heights + [0]
    for i in range(len(heights)):
        while st and heights[st[-1]] > heights[i]:
            res = max(res, heights[st.pop()] * (i - st[-1] - 1))
        st.append(i)
    return res


heights = [2,1,5,6,2,3]
print(main(heights))

heights = [2,4]
print(main(heights))