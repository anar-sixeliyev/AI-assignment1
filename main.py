import sys
from heapq import heappush, heappop

def takeInputs(fName):
    with open(fName, 'r') as file:
        first_line = file.readline().strip()
        second_line = int(file.readline().strip())
        first_line_list = [int(x) for x in first_line.split(',')]
        return (first_line_list, second_line)

#function for calculating the herustic value
def heuristic(jugs, target):
    remaining = target - jugs[-1]
    if remaining < 0:
        return float('inf')
    else:
        return 1 + remaining / len(jugs)

#function for solving the shortest path using A star algorithm
def AStarAlgorithm(capacities,target):
    #  Add a very large number to the end of the capacities list. (infinitely large jug)
    capacities = capacities + [10e6]
    heap = [(0 + abs(0 - target), 0, [0] * (len(capacities)))] 

    # create an empty set that will be used to keep track of the states that have already been visited during the search.
    passed = set()
    
    # loop that will continue as long as the heap data structure is not empty.
    while heap:
        # remove the smallest element from the heap and assigns its contents to three variables
        _, steps, jugs =  heappop(heap)
        
        # check if the last jug (the one with the largest capacity) contains the target amount of water.
        # if it does return the number of steps taken to reach this state.
        if jugs[-1] == target:
            return steps, jugs
        
        # check if the last jug contains more water than the target amount
        elif jugs[-1] > target:
            return -1

        # tuple representing the current state of the jugs to the passed set, indicating that this state has been visited during the search
        if (tuple(jugs)) in passed:
            continue
        passed.add(tuple(jugs))

        # each jug index and the value(capacity) of the current element on each iteration.
        for i, cap in enumerate(capacities):
            for j, cap2 in enumerate(capacities):
                #  check if the loop is iterating over the same jug
                if i==j:
                    continue

                new_jug = jugs[:]

                # if i is not the last cup fill it to the full capacity
                if i != len(capacities) - 1:
                    new_jug[i] = cap
                else:
                    # if j is not the last cup fill it to the full capacity
                    if j != len(capacities) - 1:
                        # pour from jug j to jug i by taking the minimum of the amount of water in jug j and the amount of space left in jug i
                        pour_amount = min(new_jug[j], cap - new_jug[i])
                        new_jug[i] += pour_amount
                        new_jug[j] -= pour_amount

                if tuple(new_jug) not in passed:
                    # print(steps, "jugs state : ", new_jug)
                    heappush(heap, (steps+heuristic(new_jug,target), steps+1, new_jug))
    return -1


def processFile():
    if len(sys.argv) != 2:
        print("Usage: python main.py <filename>")
        return

    capacities, target = takeInputs(sys.argv[1])
    steps, path = AStarAlgorithm(capacities, target)
    print("Path:", path)
    print("Steps:", steps)


processFile()