def main():
    N = list(map(int, input().split()))
    scores = list(map(int, input().split()))
    points = N[0]*N[2]
    sum_scores = sum(scores)
    nes_score = points - sum_scores

    if nes_score > N[1]:
        print(-1)
    elif nes_score < 0:
        print(0)
    else:
        print(nes_score)


if __name__ == "__main__":
    main()
