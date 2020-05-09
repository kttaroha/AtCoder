def main():
    A, B = map(int, input().split())
    num_socket = 1
    num_tap = 0 
    while num_socket < B:
        num_tap += 1
        num_socket += A - 1
    print(num_tap)


if __name__ == '__main__':
    main()
