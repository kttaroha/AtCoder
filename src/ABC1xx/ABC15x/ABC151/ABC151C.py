from collections import defaultdict


def main():
    a = list(map(int, input().split()))
    inputs = [input().split() for i in range(a[1])]
    num_ac = 0
    results = defaultdict(int)
    results_wa = defaultdict(int)
    for i in inputs:
        if not results[i[0]]:
            if i[1] == "WA":
                results_wa[i[0]] += 1
            elif i[1] == "AC":
                num_ac += 1
                results[i[0]] = 1
    
    for k in results.keys():
        if results[k] == 0:
            results_wa[k] = 0
    
    num_wa = sum(results_wa.values())
    print(num_ac, num_wa)


if __name__ == "__main__":
    main()
