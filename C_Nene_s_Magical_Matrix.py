def nene_magical_matrix(n):
    matrix = [[0 for i in range(n)] for j in range(n)]

    ans = 0
    for k in range(n):
        ans += (2 * k - 1) * k

        