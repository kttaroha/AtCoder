def main():
    N, K = map(int, input().split())
    G = list(map(int, input().split()))
    min_dist = 1e10
    for i in range(N-K+1):
        if G[i] < 0 and G[i+K-1] < 0:
            min_dist_ = abs(G[i])
        elif G[i] < 0 and G[i+K-1] >= 0:
            min_dist_ = min(2*abs(G[i])+G[i+K-1], abs(G[i])+2*G[i+K-1])
        else:
            min_dist_ = abs(G[i+K-1])

        min_dist = min(min_dist, min_dist_)

    print(min_dist)


if __name__ == '__main__':
    main()
