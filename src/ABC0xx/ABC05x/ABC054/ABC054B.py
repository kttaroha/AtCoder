def main():
    N, M = map(int, input().split())
    A = [list(input()) for _ in range(N)]
    B = [list(input()) for _ in range(M)]
    flag_true = False
    for h_move in range(N-M+1):
        for w_move in range(N-M+1):
            for h_search in range(M):
                for w_search in range(M):
                    if B[h_search][w_search] \
                        != A[h_search+h_move][w_search+w_move]:
                        break
                else:
                    continue
                break
            else:
                flag_true = True

    if flag_true:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
