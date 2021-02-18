def solution(number, k):
    st = []
    for i in range(len(number)):
        print(st, k)
        while st and k > 0 and st[-1] < number[i]:
            print(st)
            st.pop()
            k -= 1
        st.append(number[i])
    print(st)
    return ''.join(st[:len(st) - k])



solution('123456', 3)