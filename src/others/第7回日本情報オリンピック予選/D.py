def main():
    M = int(input())
    Ms = []
    relative_pos = []
    for _ in range(M):
        Ms.append(list(map(int, input().split())))

    for i in range(1, len(Ms)):
        relative_pos.append([Ms[i][0] - Ms[0][0], Ms[i][1] - Ms[0][1]])

    N = int(input())
    Ns = set()
    for _ in range(N):
        Ns.add(tuple(map(int, input().split())))

    for n in Ns:
        for r_pos in relative_pos:
            pos = (n[0] + r_pos[0], n[1] + r_pos[1])
            if pos not in Ns:
                break
        else:
            diff = (n[0] - Ms[0][0], n[1] - Ms[0][1])
            break
    print(*diff)


if __name__ == '__main__':
    main()
