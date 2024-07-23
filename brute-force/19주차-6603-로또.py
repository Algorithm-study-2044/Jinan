import sys

sys.setrecursionlimit(10**6)


def combination(k, S, start, end):
    if k == 0:
        return [[]]
    if k == 1:
        return [[S[i]] for i in range(start, end+1)]
    if start == end:
        return [[S[start]]]

    res = []
    for i in range(start, end - k + 2):
        for tail in combination(k-1, S, i+1, end):
            res.append([S[i]] + tail)
    return res


query = []
while True:
    line = list(map(int, input().strip().split()))
    k = line[0]
    if k == 0:
        break
    S = line[1:]
    query.append(S)

for S in query:
    res = combination(6, S, 0, len(S)-1)
    for comb in res:
        print(' '.join(map(str, comb)))
    print()
