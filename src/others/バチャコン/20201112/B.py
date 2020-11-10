def main():
    S = input()
    name = ""
    after_at = False
    names = []
    for s in S:
        if after_at:
            if s == "@":
                names.append(name)
                name = ""
            elif s == " ":
                after_at = False
                names.append(name)
                name = ""
            else:
                name += s
        else:
            if s == "@":
                after_at = True
    else:
        names.append(name)

    names = sorted(list(set(names)))

    for name in names:
        if name != "":
            print(name)


if __name__ == '__main__':
    main()
