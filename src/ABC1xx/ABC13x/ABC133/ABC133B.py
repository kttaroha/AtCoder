def main():
    N, D = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]    
    cnt = 0
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            a1 = A[i]
            a2 = A[j]
            dist = 0
            for x, y in zip(a1, a2):
                dist += (x-y)**2
            dist_sqr = dist**0.5
            if dist_sqr == int(dist_sqr):
                cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
