def main():
    N = int(input())
    S = input()
    ans = 1e5
    for i in range(N):
        left_S = S[:i]
        right_S = S[i:]
        grid = [[0] * (len(left_S)+1) for _ in range(len(right_S)+1)]
        for left in range(1, len(left_S)+1):
            for right in range(1, len(right_S)+1):
                if right_S[right-1] == left_S[left-1]:
                    grid[right][left] = grid[right-1][left-1] + 1
                else:
                    grid[right][left] = max(
                        grid[right-1][left], grid[right][left-1])

        ans = min(ans, N - 2*grid[len(right_S)][len(left_S)])

    print(ans)


if __name__ == '__main__':
    main()
