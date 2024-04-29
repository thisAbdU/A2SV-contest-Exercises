def giveaway(queries, items):
    items = sorted(items, reverse=True)
    cheap = (items[:queries[0]])[:-(queries[1] + 1):-1]
    total = sum(cheap)
    return total

item_query = list(map(int, input().split()))
items = list(map(int, input().split()))
for i in range(item_query[1]):
    queries = list(map(int, input().split()))
    print(giveaway(queries, items))

                                                                           