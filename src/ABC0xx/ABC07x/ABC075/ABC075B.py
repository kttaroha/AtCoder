def main():
    H, W = map(int, input().split())
    board = [list(input()) for _ in range(H)]
    new_board = []
    for i in range(H):
        new_line = ""
        for j in range(W):
            num_bomb = 0
            if board[i][j] != "#":
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        idx1, idx2 = i+k, j+l
                        if idx1 >= 0 and idx2 >= 0 and idx1 < H and idx2 < W:
                            item = board[i+k][j+l]
                            if item == "#":
                                num_bomb += 1
                new_line += str(num_bomb)
            else:
                new_line += "#"

        new_board.append(new_line)

    for i in range(H):
        print(new_board[i])


if __name__ == '__main__':
    main()
