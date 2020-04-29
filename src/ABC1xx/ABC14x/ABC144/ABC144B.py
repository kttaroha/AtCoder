def main():
    n = int(input())
    flag = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if n == i*j:
                print("Yes")
                flag += 1
                break
        else:
            continue
        break
    if not flag:
        print("No")


if __name__ == "__main__":
    main()
