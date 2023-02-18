from heapq import heappush, heappop
import sys

# def heuristic(current_state,target_quantity):
#     return abs(sum(current_state) - target_quantity)

def heuristic(current_state,target_quantity):
    #getting the infinite capacity pitcher
    inifinite_capacity_pitcher = current_state[-1]

    #comparing the infinite capacity pitcher with target 
    #if it is less than target we return differente between them, else we just return maximum value
    if inifinite_capacity_pitcher <= target_quantity:
        return target_quantity - inifinite_capacity_pitcher
    
    return sys.maxsize

def shortest_path(capacities, target):
    capacities = capacities + [10e6]
    heap = [(0 + abs(0 - target), 0, [0] * (len(capacities)))]  # (steps + heuristic, steps, jugs)
    visited = set()

    while heap:
        _, steps, jugs = heappop(heap)
        if jugs[-1]== target:
            return steps, jugs
        
        # if (amount, tuple(jugs)) in visited:
        #     continue
        print(steps, jugs)
        visited.add(tuple(jugs))
        for i, cap in enumerate(capacities):
            for j, cap2 in enumerate(capacities):
                if i == j:
                    continue
                new_jugs = jugs[:]

                pour = min(capacities[i],capacities[j])

                #if we can pour from one cup to other without overflowing or underflowing
                #and if it is not the inifinity capacity pitcher then we pour it
                if new_jugs[i]+pour <= capacities[i] and new_jugs[j]-pour >= 0 and j!=len(capacities)-1:
                    new_jugs[i]+=pour
                    new_jugs[j]-=pour
                
                #in other case, if it is not the infinity capacity pitcher, we just fill it with water.
                elif i!=len(capacities)-1:
                        new_jugs[i] = capacities[i]

                #if next state is not in visited_state then we can push the new state to the queue
                if tuple(new_jugs) not in visited:
                    heappush(heap, (steps+1+heuristic(new_jugs,target), steps+1, new_jugs))

    return -1

capacities = [1,3,5]
target = 10

# capacities = [5,10,20]
# target = 15

capacities = [1,5]
target = 10

capacities = [2,5,6,72]
target = 143

# capacities = [2,3,5,19,121,852]
# target = 11443

# capacities = [3, 6]
# target = 2

steps = shortest_path(capacities, target)
print("Steps:", steps)
# print("Path:", path)