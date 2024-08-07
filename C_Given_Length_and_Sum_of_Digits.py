def find_min_and_max(m, s):
    if s < 1 and m > 1 or s > m * 9:
        return -1, -1

    # Finding min
    minn = ""
    for i in range(m):
        j = max(0, s - 9 * (m - i - 1))
        if i == 0 and j == 0 and s:
            j = 1
        minn += str(j)
        s -= j

    # Finding max
    maxx = ""
    for i in range(m):
        j = min(9, s)
        maxx += str(j)
        s -= j

    return int(minn), int(maxx)

m_s = list(map(int, input().split()))
m, s = m_s
print(*find_min_and_max(m, s))
