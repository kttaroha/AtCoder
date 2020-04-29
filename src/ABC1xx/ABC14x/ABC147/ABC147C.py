from collections import defaultdict


def main():
    N = int(input())
    d = defaultdict(list)
    for i in range(N):
        n = int(input())
        for _ in range(n):
            d[i].append(list(map(int, input().split())))
    max_trust_num = 0

    # check all possible combinations of Honest or Unkind.
    for i in range(2**N):
        trust = True

        # assign Honest or Unnkind to each person.
        # if person i is Honest, trust_combs[i] = 1
        # else, trust_combs[i] = 0
        trust_combs = []
        for j in range(N):
            if (i >> j) & 1:
                trust_combs.append(1)
            else:
                trust_combs.append(0)
  
        # check if the combination of Honest or
        # Unkind contradicts the given statements.
        for k in range(len(trust_combs)):
            if trust_combs[k] == 1:
                for l in d[k]:
                    if not l[1] == trust_combs[l[0]-1]:
                        trust = False
        if trust:
            max_trust_num = max(max_trust_num, sum(trust_combs))

    print(max_trust_num)


if __name__ == "__main__":
    main()
