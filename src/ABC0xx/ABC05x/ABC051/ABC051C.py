def main():
    sx, sy, tx, ty = map(int, input().split())
    move1 = []
    move2 = []
    for i in range(abs(sx-tx)):
        if sx > tx:
            move1.append("L")
        else:
            move1.append("R")

    for j in range(abs(sy-ty)):
        if sy > ty:
            move2.append("D")
        else:
            move2.append("U")

    move3 = [reverse(m) for m in move1]
    move4 = [reverse(m) for m in move2]

    move5 = [reverse(move2[0])] + move1
    move5.append(move1[-1])

    move6 = [move2[0]] + move2
    move6.append(reverse(move1[0]))

    move7 = [reverse(m) for m in move5]
    move8 = [reverse(m) for m in move6]

    move = move1 + move2 + move3 + move4 + move5 + move6 + move7 + move8
    move_str = ""

    for m in move:
        move_str += m
    print(move_str)


def reverse(m):
    if m == "D":
        return "U"
    elif m == "U":
        return "D"
    elif m == "R":
        return "L"
    else:
        return "R"


if __name__ == '__main__':
    main()
