N, M = map(int, input().split())

paper = [list(input()) for _ in range(N)]

answer = []

for i in range(0, N - 7):
    for j in range(0, M - 7):
        white = 0
        black = 0
        for r in range(i, i + 8):
            for c in range(j, j + 8):
                if (r+c) % 2 == 0:
                    if paper[r][c] != 'W':
                        white += 1
                    else:
                        black += 1
                else:
                    if paper[r][c] != 'B':
                        white += 1
                    else:
                        black += 1
        answer.append(white)
        answer.append(black)
        
print(min(answer))