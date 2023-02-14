import numpy as np
from heapq import heappush, heappop

def heuristic_(current_state, target):
    return np.abs(np.sum(current_state) - target)

def shortest_path(capacities, target):
    heap = [(0 + abs(0 - target), 0, 0, [0] * len(capacities))]  # (steps + heuristic, steps, amount, jugs)
    visited = set()

    while heap:
        heuristic , steps, amount, jugs = heappop(heap)
        print("Visited state: ", steps, jugs)
        if amount == target:
            return steps, jugs
        if (amount, tuple(jugs)) in visited:
            continue
        visited.add((amount, tuple(jugs)))

        for i, cap in enumerate(capacities):
            for j, cap2 in enumerate(capacities):

                if i == j:
                    continue
                new_jugs = jugs[:]
                print("new jugs before: ",new_jugs[i], new_jugs[j])
                new_jugs[i] = cap# - new_jugs[i]
                # new_jugs[j] = min((new_jugs[j] + amount), target)
                print("new jugs after: ",new_jugs[i], new_jugs[j], target)

                heappush(heap, (steps + 1 + heuristic_(new_jugs, target), steps + 1, new_jugs[i], new_jugs))

                new_jugs = jugs[:]
                # print("new jugs before: ",new_jugs[i], new_jugs[j])

                if new_jugs[i] + new_jugs[j] <= cap2:
                    new_jugs[j] += new_jugs[i]
                    new_jugs[i] = 0
                else:
                    diff = cap2 - new_jugs[j]
                    new_jugs[j] = cap2
                    new_jugs[i] -= diff
                heappush(heap, (steps + 1 + abs(new_jugs[j] - target), steps + 1, new_jugs[j], new_jugs))

    return -1, []

# capacities = [20,10,5]
# target = 15
capacities = [1,3,5]
target = 17
steps, path = shortest_path(capacities, target)
print("Steps:", steps)
print("Path:", path)
