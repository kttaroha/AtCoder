def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(M)]
    min_cards = 1
    max_cards = N
    for i in range(len(A)):
        min_cards = max(A[i][0], min_cards)
        max_cards = min(A[i][1], max_cards)

    if min_cards > max_cards:
        print(0)
    else:
        print(max_cards - min_cards + 1)


if __name__ == '__main__':
    main()
