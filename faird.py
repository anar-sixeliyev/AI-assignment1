import sys
import numpy as np
import heapq

def read_file(filename):
    with open(filename,"r") as f:
        capacities = np.array(f.readline().split(","))
        target = int(f.readline())
    return capacities.astype(np.int32), target

def simple_heuristic(current_state,target_quantity):
    # current_quantity = current_state[-1]
    # if current_quantity < target_quantity:
    #     return target_quantity - current_quantity
    # else:
    #     return 0
    return np.abs(np.sum(current_state) - target_quantity)

def A_star_algorithm(capacities,target_quantity):
    #pass
    capacities = np.append(capacities, sys.maxsize)
    initial_state = list(np.zeros(capacities.shape, dtype = np.int32))
    initial_heuristic = simple_heuristic(initial_state,target_quantity)
    initial_step = 0
    
    fridge_pq = [(initial_heuristic, 0, initial_state)]
    
    visited_states = set()

    while fridge_pq:
        heuristic,step,current_state =  heapq.heappop(fridge_pq)

        # print(step, current_state)
 
        if current_state[-1] == target_quantity:
           return step


        # print("Visited state: ",tuple(current_state))
        visited_states.add(tuple(current_state))

        # print()
        for i in range(capacities.shape[0]):
            for j in range(capacities.shape[0]):
                if i==j:
                    continue
                next_state = current_state.copy()
                pour = min(capacities[i],capacities[j])
                if next_state[i]+pour <= capacities[i] and next_state[j]-pour >= 0:
                    next_state[i]+=pour
                    next_state[j]-=pour
                    print("inside if  state: ",next_state[i], next_state[j])

                else:
                    if i!=capacities.shape[0]-1:
                        next_state[i] = capacities[i] - next_state[i]
                        print("inside else  state: ",next_state[i])

                if tuple(next_state) not in visited_states:
                    # print((step+1+simple_heuristic(next_state,target_quantity), 
                    #                step+1, next_state))
                    heapq.heappush(fridge_pq, (step+1+simple_heuristic(next_state,target_quantity), 
                                   step+1, next_state))

    return -1


capacities, target_quantity = read_file('sample01.txt')
print(A_star_algorithm(capacities,target_quantity))

#Command transiver, ground #NECE S