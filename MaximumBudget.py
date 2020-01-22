def solution(d, budget):
    d.sort()
    cnt = 0
    total = 0
    for i in d:
        total += i
        if total > budget:
            return cnt
        else:
            cnt += 1
    return cnt
