from decimal import Decimal


def main():
    tmp = input().split()
    A = int(tmp[0])
    B = Decimal(tmp[1])
    A = Decimal(A)
    B = Decimal(B)
    print(int(A*B))


if __name__ == '__main__':
    main()
