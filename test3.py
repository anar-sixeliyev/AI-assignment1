from heapq import heappush, heappop

def simple_heuristic(current_state,target_quantity):
    return abs(sum(current_state) - target_quantity)

def shortest_path(capacities, target):
    heap = [(0 + abs(0 - target), 0, [0] * (len(capacities)+1))]  # (steps + heuristic, steps, jugs)
    visited = set()

    while heap:
        _, steps, jugs = heappop(heap)
        if jugs[-1]== target:
            return steps, jugs
        
        # if (amount, tuple(jugs)) in visited:
        #     continue
        
        visited.add(tuple(jugs))
        for i, cap in enumerate(capacities):
            for j, cap2 in enumerate(capacities):
                if i == j:
                    continue
                new_jugs = jugs[:]

                new_jugs[j] = cap2

                if tuple(new_jugs) not in visited:
                    heappush(heap, (steps + 1 + simple_heuristic(new_jugs, target), steps + 1, amount, new_jugs))

                new_jugs = jugs[:]
                if new_jugs[i] + new_jugs[j] <= cap2:
                    new_jugs[j] += new_jugs[i]
                    new_jugs[i] = 0
                else:
                    diff = cap2 - new_jugs[j]
                    new_jugs[j] = cap2
                    new_jugs[i] -= diff
                if tuple(new_jugs) not in visited:
                    heappush(heap, (steps + 1 + simple_heuristic(new_jugs, target), steps + 1, amount, new_jugs))

                new_jugs = jugs[:]
                if(new_jugs[j]> 0):
                    amount += new_jugs[j]
                    new_jugs[j] = 0
                    if tuple(new_jugs) not in visited:
                        heappush(heap, (steps + 1 + simple_heuristic(new_jugs, target), steps + 1, amount, new_jugs))

    return -1, []

capacities = [1,3,5]
target = 10

# capacities = [5,10,20]
# target = 15

capacities = [1,5]
target = 10

# capacities = [2,5,6,72]
# target = 143

# capacities = [2,3,5,19,121,852]
# target = 11443

# capacities = [3, 6]
# target = 2

steps, path = shortest_path(capacities, target)
print("Steps:", steps)
print("Path:", path)