import unittest
from math import inf
from main import heuristic, AStarAlgorithm
from heapq import heappush, heappop

class TestHeuristic(unittest.TestCase):

    def test_admissible(self):
        jugs = [0, 0, 0]
        target = 8
        self.assertLessEqual(heuristic(jugs, target), 8)

        jugs = [3, 3, 3]
        target = 8
        self.assertLessEqual(heuristic(jugs, target), 3)

        jugs = [2, 2, 2]
        target = 5
        self.assertLessEqual(heuristic(jugs, target), 2)

        jugs = [1, 1, 1]
        target = 5
        self.assertLessEqual(heuristic(jugs, target), 4)

    # small implementation of A* to obtain more realistic output
    def test_consistent(self):
        jugs = [1, 3, 5]
        target = 17
        h_old = heuristic(jugs, target)
        passed = set()
        heap = [(h_old, 0, jugs)]

        while heap:
            _, steps, jugs = heappop(heap)
            if jugs[-1] == target:
                break
            elif jugs[-1] > target:
                return -1
            passed.add(tuple(jugs))

            for i, cap in enumerate(jugs):
                for j, cap2 in enumerate(jugs):
                    if i==j:
                        continue

                    new_jug = jugs[:]
                    if i != len(jugs) - 1:
                        new_jug[i] = cap
                    else:
                        if j != len(jugs) - 1:
                            pour_amount = min(new_jug[j], cap - new_jug[i])
                            new_jug[i] += pour_amount
                            new_jug[j] -= pour_amount

                    h = heuristic(new_jug, target)
                    self.assertLessEqual(steps + h, heuristic(jugs, target) + 1)
                    
                    if tuple(new_jug) not in passed:
                       heappush(heap, (steps + h, steps + 1, new_jug))
                    
class TestAStarAlgorithm(unittest.TestCase):
    def test_AStarAlgorithm_1(self):
        capacities = [5, 10, 20]
        target = 15
        expected_result = (4, [0, 0, 0, 15])
        actual_result = AStarAlgorithm(capacities, target)
        self.assertEqual(actual_result, expected_result)

    def test_AStarAlgorithm_2(self):
        capacities = [1,4,10,15,22]
        target = 181
        expected_result = (20, [0, 0, 0, 0, 0, 181])
        actual_result = AStarAlgorithm(capacities, target)
        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()
