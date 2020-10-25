from collections import defaultdict


def main():
    N = int(input())
    A = list(map(int, input().split()))
    d = defaultdict(list)
    num = [0] * (2*N - 1)
    for i in range(2*N):
        d[A[i]].append(i)
    
    for k in d.keys():
        diff = abs(d[k][1] - d[k][0]) - 1
        
        num[diff] += 1

    ans = 0
    for i in range(len(num)):
        ans += num[i]
        print(ans)


if __name__ == '__main__':
    main()