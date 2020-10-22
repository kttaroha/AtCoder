import math


def check_keta(num):
    if num > 1:
        return int(math.log10(num))+1
    elif num == 1:
        return 1
    else:
        return 0


def main():
    N = int(input())
    limit = int(N ** 0.5)
    min_keta = 1e10
    for i in range(1, limit+1):
        if N % i == 0:
            keta = 0
            keta = max(check_keta(N // i), check_keta(i))
            min_keta = min(min_keta, keta)
    print(min_keta)


if __name__ == '__main__':
    main()
