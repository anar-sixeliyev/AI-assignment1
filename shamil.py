import sys
from heapq import heappush, heappop

def read_file(filename):
    with open(filename, 'r') as file:
        first_line = file.readline().strip()
        second_line = int(file.readline().strip())
        first_line_list = [int(x) for x in first_line.split(',')]
        return (first_line_list, second_line)

#function for calculating the herustic value
def heuristic(jugs,target_quantity):
    #getting the infinite capacity pitcher
    inifinite_capacity_pitcher = jugs[-1]

    #comparing the infinite capacity pitcher with target 
    #if it is less than target we return differente between them, else we just return maximum value
    if inifinite_capacity_pitcher <= target_quantity:
        return target_quantity - inifinite_capacity_pitcher
    
    return sys.maxsize

def h2(jugs, target):
    return sum((target - jug) / cap for jug, cap in zip(jugs, capacities))


def h1(state, goal, capacities):
    if(goal<0):
        return sys.maxsize
    total_volume = sum(state)
    remaining_volume = goal - total_volume
    min_steps = 0
    for i in range(0,len(capacities)-1):
        min_steps += remaining_volume // capacities[i]
        remaining_volume = remaining_volume % capacities[i]
    return min_steps

#function for solving the shortest path using A star algorithm
def a_star_algorithm(capacities,target):
    capacities = capacities + [10e6]
    heap = [(0 + abs(0 - target), 0, [0] * (len(capacities)))] 
    visited_states = set()
    
    while heap:
        _ , steps, jugs =  heappop(heap)
        
        if jugs[-1] == target:
            return steps
        
        elif jugs[-1] > target:
            return -1

        visited_states.add(tuple(jugs))

        for i, cap in enumerate(capacities):
            for j, cap2 in enumerate(capacities):
                if i==j:
                    continue

                new_jug = jugs[:]

                if i != len(capacities) - 1:
                        new_jug[i] = cap
                else:
                    if j != len(capacities) - 1:
                        pour_amount = min(new_jug[j], cap - new_jug[i])
                        new_jug[i] += pour_amount
                        new_jug[j] -= pour_amount
                    else:
                        new_jug[i] = cap

                if tuple(new_jug) not in visited_states:
                    # heappush(heap, (steps+1+h1(new_jug,target-new_jug[-1],capacities), steps+1, new_jug))
                    heappush(heap, (steps+1+heuristic(new_jug,target), steps+1, new_jug))

    return -1


# capacities = [5, 10, 20]
# target = 15

capacities, target = read_file('sample01.txt')
steps = a_star_algorithm(capacities, target)
print("Steps:", steps)