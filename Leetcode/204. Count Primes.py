def countPrimes(n) -> int: #428ms
    if n <= 2:
        return 0
    isPrime = [True] * n
    i = 2
    while i * i < n:
        if isPrime[i]:
            for j in range(i * 2, n, i):
                isPrime[j] = False
        i += 1

    return sum(isPrime[2:])

countPrimes(10)
#countPrimes(1500000)



class Solution: # 212ms
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        isPrime = [1] * n
        isPrime[0] = isPrime[1] = 0
        for i in range(2, int(n**0.5) + 1):
            if isPrime[i]:
                isPrime[i * i: n : i] = [0] * len(isPrime[i * i: n : i])
        return sum(isPrime)