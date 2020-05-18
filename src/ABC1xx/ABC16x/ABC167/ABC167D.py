def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    prev_p = 1
    g = []
    seen = [0]*N
    i = 0
    while True:
        if seen[prev_p-1]:
            break
        seen[prev_p-1] = i
        g.append(A[prev_p-1])
        prev_p = g[-1]
        i += 1
    g_periodic = g[seen[prev_p-1]:]  
    g_before = g[:seen[prev_p-1]]

    if K <= len(g_before):
        print(g_before[K-1])
    else:
        K_new = (K - len(g_before)) % len(g_periodic)
        print(g_periodic[K_new-1])


if __name__ == '__main__':
    main()
