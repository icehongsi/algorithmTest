def solution(number, k):
    st = []
    for i in range(len(number)):
        print(st, k)
        while st and k > 0 and st[-1] < number[i]: #st에 숫자가 있고 더 들어갈 공간이 있을 경우, 배열 마지막 원소와 숫자를 비교한다.
            print(st)
            st.pop() # 계속 숫자 제거해가기
            k -= 1
        st.append(number[i])
    print(st)
    return ''.join(st[:len(st) - k])



solution("4177252841", 4)