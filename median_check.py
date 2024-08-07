import heapq


def median_check(minarr, maxarr, med, budget):
    n, k = len(minarr), len(med)
    minis = 0
    for _ in n:
        if budget > 0:
            curr = heapq.heappop(minarr)
            minis += curr
            budget -= curr
