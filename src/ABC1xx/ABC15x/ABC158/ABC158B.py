def main():
    N, A, B = map(int, input().split())
    print(N // (A + B) * A + min(N % (A + B), A))


if __name__ == "__main__":
    main()
