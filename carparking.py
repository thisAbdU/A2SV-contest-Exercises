from collections import defaultdict
import heapq

def find_the_nearest_parking_slot(query, n):
    slots = [i for i in range(1, n + 1)]
    heapq.heapify(slots)
    num_car = defaultdict(int)
    
    for q in query:
        if q[0] == 'L': 
            if q[1] in num_car:
                heapq.heappush(slots, num_car[q[1]])
                del num_car[q[1]] 
            
        elif q[0] == 'E': 
            if slots:
                near = heapq.heappop(slots)
                print(f"Good morning sir, please proceed to slot number {near}")
                num_car[q[1]] = near 
            else:
                print("Sorry sir, no available slots")
    return 


n = int(input())
q = int(input())
queries = []

for _ in range(q):
    wh, car_id = input().split()
    queries.append([wh, car_id])

find_the_nearest_parking_slot(queries, n)
