def sol():
    col, row = int(input()), int(input())
    ordered = list(input())
    board = [list(input()) for _ in range(row)]
    order = sorted(ordered)

    # top-down
    for i in range(row):
        if board[i][0] == "?":
            break
        for j in range(col - 1):
            if board[i][j] == "-": #swap
                order[j], order[j+1] = order[j+1], order[j]

    for i in range(row-1, -1, -1):
        if board[i][0] == "?":
            break
        for j in range(col - 1):
            if board[i][j] == "-": #swap
                ordered[j], ordered[j+1] = ordered[j+1], ordered[j]

    #comparison
    answer = ""

    for i in range(len(ordered) - 1):

        if ordered[i] == order[i]:
            answer += "*"
        else:
            order[i], order[i+1] = order[i+1], order[i]
            answer += "-"

    return answer if ordered == order else "x" * (len(ordered) - 1)

print(sol())