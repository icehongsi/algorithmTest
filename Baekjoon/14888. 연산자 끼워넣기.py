def solve(num, i = 1):
    global max_val, min_val
    if i == n:
        max_val = max(max_val, num)
        min_val = min(min_val, num)
        return
    for o in op:
        if op[o]:
            op[o] -= 1
            if o == "//" and num < 0 and numbers[i] > 0:
                solve(-eval(f"{-num}//{numbers[i]}"), i+1)
            else:
                solve(eval(f"{num}{o}{numbers[i]}"), i+1)

            op[o] += 1

n = int(input())
numbers = list(map(int, input().split()))
op = dict(zip(["+", "-", "*", "//"], list(map(int, input().split()))))
min_val, max_val = float('inf'), -float('inf')
solve(numbers[0])
print(max_val, min_val, sep = "\n")