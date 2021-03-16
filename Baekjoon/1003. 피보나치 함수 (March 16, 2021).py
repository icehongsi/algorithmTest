def solution():
    answer_0, answer_1 = [], []

    def fib(n):
        dp_0, dp_1 = [1, 0], [0, 1]
        if n < 2:
            answer_0.append(dp_0[n])
            answer_1.append(dp_1[n])
            return
        for i in range(2, n + 1):
            dp_0 = [dp_0[1], dp_0[0] + dp_0[1]]
            dp_1 = [dp_1[1], dp_1[0] + dp_1[1]]

        answer_0.append(dp_0[-1])
        answer_1.append(dp_1[-1])

    for i in range(int(input())):
        fib(int(input()))

    for i in range(len(answer_0)):
        print(answer_0[i], answer_1[i], sep=" ")


solution()

