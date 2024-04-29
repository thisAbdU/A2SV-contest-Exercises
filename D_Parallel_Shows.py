
def parallel_shows(shows):
    def find_max(arr):
        max_ = 0
        for i in range(len(arr)):
            if shows[i][1] > max_:
                max_ = shows[i][1]
        return max_

    prefix = [0 for i in range(find_max(shows))]
    for i in range(n):
        for j in range(shows[i][0] - 1, shows[i][1]):
            prefix[j] += 1

    if 4 in prefix:
        return "NO"
    else:
        return "YES"
    

n = int(input())
shows = []
for i in range(n):
    show = list(map(int, input().split()))
    shows.append(show)
print(parallel_shows(shows))