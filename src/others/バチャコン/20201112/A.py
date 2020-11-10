def main():
    S = input()
    if len(set(S)) == len(S):
        print("yes")
    else:
        print("no")


if __name__ == '__main__':
    main()
