def fib(n):
    dp_0, dp_1 = [1, 0], [0, 1]
    for i in range(2, n+1):
        dp_0.append(dp_0[-1] + dp_0[-2])
        dp_1.append(dp_1[-1] + dp_1[-2])

    print(dp_0[n], dp_1[n], sep=" ")


tc = []
for i in range(int(input())):
    tc.append(int(input()))
for i in tc:
    fib(i)