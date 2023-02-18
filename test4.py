import numpy as np
import heapq
import os

#function for reading the file and collecting the capacities to numpy array
#and converting the target quantity to integer value
def read_file(filename):
    with open(filename,"r") as f:
        capacities = np.array(f.readline().split(","))
        target = int(f.readline())
    return capacities.astype(np.int32), target

#function for calculating the herustic value
def heuristic(current_state,target_quantity):
    #getting the infinite capacity pitcher
    inifinite_capacity_pitcher = current_state[-1]

    #comparing the infinite capacity pitcher with target 
    #if it is less than target we return differente between them, else we just return maximum value
    if inifinite_capacity_pitcher <= target_quantity:
        return target_quantity - inifinite_capacity_pitcher
    
    return sys.maxsize


#function for solving the shortest path using A star algorithm
def a_star_algorithm(capacities,target_quantity):
    #appending the pitcher with maximum capacity
    capacities = np.append(capacities, sys.maxsize)
    
    #initializing the capacities with zero values
    initial_state = list(np.zeros(capacities.shape, dtype = np.int32))

    #initial heuristic distance between the initial state and goal state
    initial_heuristic = heuristic(initial_state,target_quantity)
    
    #initializing the step with zero
    initial_step = 0

    #initializing the fridge by adding the initial tuple
    fridge_pq = [(initial_heuristic+initial_step, initial_step, initial_state)]

    #initializing the visited_states set
    visited_states = set()
    
    while fridge_pq:

        #popping the tuple from the priority queue
        h , step, current_state =  heapq.heappop(fridge_pq)
        
        #print(h, step, current_state)
        
        #checking if the infinite capacity pitcher has a water or not
        if current_state[-1] == target_quantity:
           return step
        
        #checking if infinite capacity pitcher has a higher value than target
        elif current_state[-1] > target_quantity:
            return -1

        #adding the state to the visited_states set
        visited_states.add(tuple(current_state))

        for i in range(capacities.shape[0]):
            for j in range(capacities.shape[0]):
                #if pitchers are same, we don't do anything just continue
                if i==j:
                    continue

                #copying the state for next state
                next_state = current_state.copy()

                #finding the minimum between capacities for pouring the water
                pour = min(capacities[i],capacities[j])

                #if we can pour from one cup to other without overflowing or underflowing
                #and if it is not the inifinity capacity pitcher then we pour it
                if next_state[i]+pour <= capacities[i] and next_state[j]-pour >= 0 and j!=capacities.shape[0]-1:
                    next_state[i]+=pour
                    next_state[j]-=pour
                
                #in other case, if it is not the infinity capacity pitcher, we just fill it with water.
                else:
                    if i!=capacities.shape[0]-1:
                        next_state[i] = capacities[i]

                #if next state is not in visited_state then we can push the new state to the queue
                if tuple(next_state) not in visited_states:
                    heapq.heappush(fridge_pq, (step+1+heuristic(next_state,target_quantity), 
                                   step+1, next_state))

    return -1


def main():
    #cheking if user added the name of file or not
    if len(sys.argv)==1:
        raise Exception("Please add the second argument for the name of the file")
    
    #reading the argument as filename
    filename = sys.argv[1]

    #checking the existence of the file
    if not os.path.isfile(filename):
        raise FileExistsError("File do not exist")