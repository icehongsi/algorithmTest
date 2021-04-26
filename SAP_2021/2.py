count = 0
while True:
    ans = []
    n = int(input())
    if n == 0:
        break
    box = []
    for i in range(n):
        temp = input().split()
        for i in range(len(temp)-1):
            temp[i] = float(temp[i])
        box.append(temp)
    m = int(input())
    peanuts = []
    for i in range(m):
        temp = input().split()
        for i in range(len(temp)-1):
            temp[i] = float(temp[i])
        peanuts.append(temp)

    answer = []
    for r, c, size in peanuts:
        flag = False
        for i in range(len(box)):
            if box[i][0] <= r <= box[i][2] and box[i][1] <= c <= box[i][3]:
                if box[i][-1] == size:
                    answer.append(f"{size} correct")
                    flag = True
                    break
                else:
                    answer.append(f"{size} {box[i][-1]}")
                    flag = True
                    break
        if not flag:
            answer.append(f"{size} floor")

    for a in answer:
        print(a)
    print("\n")


