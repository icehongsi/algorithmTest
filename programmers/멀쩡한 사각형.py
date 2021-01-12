import math
def solution(w,h):
    gcd = math.gcd(w, h)
    if w > h:
        w2, h2, slope = w/gcd, h/gcd, h/w
    else:
        w2, h2, slope = h/gcd, w/gcd, w/h
    area = 0
    for i in range(int(h2)):
        area += (math.ceil((i+1)/slope) - math.trunc(i / slope))
    return w * h - area * gcd

print(solution(53,47))



from math import gcd
def solution(w,h):
    return w * h - (w/gcd(w, h) + h/gcd(w, h) - 1) * gcd(w, h)


print(solution(53,47))