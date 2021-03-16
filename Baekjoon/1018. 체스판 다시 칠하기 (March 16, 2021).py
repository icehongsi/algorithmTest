def solution():
    row, col = map(int, input().split())
    board = []
    for _ in range(row):
        board.append(list(input()))

    def check_score(odd, even):
        answer = row * col
        score = [[0] * col for _ in range(row)]
        for r in range(row):
            for c in range(col):
                if ((r + c) % 2 == 1 and board[r][c] != odd) or ((r + c) % 2 == 0 and board[r][c] != even):
                    score[r][c] = 1

        for r in range(row - 7):
            for c in range(col - 7):
                answer = min(answer, (sum(sum(score[i][c : c+8]) for i in range(r, r+8))))

        return answer

    print(min(check_score("B", "W"), check_score("W", "B")))

solution()

