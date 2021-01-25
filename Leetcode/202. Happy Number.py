import time
def isHappy(n):
    results = set()
    while n != 1:
        n = sum(map(lambda x: int(x) ** 2, list(str(n))))
        if n in results:
            return False
        results.add(n)
    return True

isHappy(2)