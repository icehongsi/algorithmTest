def rangeBitwiseAnd(m, n):
    if n-m <= 1:
        return 0
    pivot = 1
    while m + pivot < n:
        pivot *= 2
    print(n & pivot)

rangeBitwiseAnd(1,4)