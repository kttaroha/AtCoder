def main():
    S = input()
    output = ""
    for s in S:
        if s == '0' or s == "1":
            output += s
        else:
            if len(output) > 0:
                output = output[:-1]

    print(output)


if __name__ == '__main__':
    main()