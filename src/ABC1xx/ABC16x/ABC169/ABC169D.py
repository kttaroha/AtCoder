from collections import defaultdict


def main():
    n = int(input())
    d = prime_factorize(n)
    cnt = 0
    for k in d.keys():
        cnt_tmp = 1
        while cnt_tmp <= d[k]:
            d[k] -= cnt_tmp
            cnt_tmp += 1
            cnt += 1
    print(cnt)


def prime_factorize(n):
    a = defaultdict(int)
    while n % 2 == 0:
        a[2] += 1
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a[f] += 1
            n //= f
        else:
            f += 2
    if n != 1:
        a[n] += 1
    return a


if __name__ == '__main__':
    main()
