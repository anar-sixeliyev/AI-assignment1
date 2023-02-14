from heapq import heappush, heappop

def read_file(filename):
    with open(filename, 'r') as file:
        first_line = file.readline().strip()
        second_line = int(file.readline().strip())
        first_line_list = [int(x) for x in first_line.split(',')]
        return (first_line_list, second_line)


def shortest_path(capacities, target):
    heap = [(0 + abs(0 - target), 0, 0, [0] * len(capacities))]  # (steps + heuristic, steps, amount, jugs)
    visited = set()

    while heap:
        _, steps, amount, jugs = heappop(heap)
        # print (_, steps, amount, jugs)
        if amount == target:
            return steps, jugs
        if (amount, tuple(jugs)) in visited:
            continue
        visited.add((amount, tuple(jugs)))
        print("Visited state: ",visited)

        for i, cap in enumerate(capacities):
            for j, cap2 in enumerate(capacities):
                if i == j:
                    continue
                new_jugs = jugs[:]
                new_jugs[i] = cap
                if new_jugs[j] + amount <= cap2:
                    new_jugs[j] += amount
                else:
                    diff = cap2 - new_jugs[j]
                    new_jugs[j] = cap2
                    new_jugs[i] -= diff
                heappush(heap, (steps + 1 + abs(new_jugs[j] - target), steps + 1, new_jugs[j], new_jugs))

                new_jugs = jugs[:]
                if new_jugs[i] + new_jugs[j] <= cap2:
                    new_jugs[j] += new_jugs[i]
                    new_jugs[i] = 0
                else:
                    diff = cap2 - new_jugs[j]
                    new_jugs[j] = cap2
                    new_jugs[i] -= diff
                heappush(heap, (steps + 1 + abs(new_jugs[j] - target), steps + 1, new_jugs[j], new_jugs))

    return -1, []

# capacities = [20, 10, 5]
# target = 15
capacities, target = read_file('sample01.txt')
steps, path = shortest_path(capacities, target)

print("Steps:", steps)
print("Path:", path)
