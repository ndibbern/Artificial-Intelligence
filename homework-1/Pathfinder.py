'''
The Pathfinder class is responsible for finding a solution (i.e., a
sequence of actions) that takes the agent from the initial state to the
optimal goal state.

This task is done in the Pathfinder.solve method, as parameterized
by a maze pathfinding problem, and is aided by the SearchTreeNode DS.
'''

from MazeProblem import MazeProblem
from SearchTreeNode import SearchTreeNode
import unittest
import heapq

class Pathfinder:

    def getSolution(node):
        soln = []
        while node.parent is not None:
            soln.append(node.action)
            node = node.parent
        soln.reverse()
        return soln

    @staticmethod
    def solve(problem):
        # Setup
        frontier = []
        explored = []
        initial_heuristic_cost = problem.heuristic(problem.initial)

        # Search
        heapq.heappush(frontier, SearchTreeNode(problem.initial, None, None, 0, initial_heuristic_cost))

        while any(frontier):
            # Get front of queue
            expanding = heapq.heappop(frontier)
            if expanding.state not in explored:
                explored.append(expanding.state)
            else:
                continue

            # Test for goal state
            if problem.goalTest(expanding.state):
                return Pathfinder.getSolution(expanding)

            # Generate new nodes on frontier
            # ('R', cost i.e. 3, (new_row, new_col))
            for transition in problem.transitions(expanding.state):
                action, cost, final_state = transition
                child_node = SearchTreeNode(final_state, \
                                            action, \
                                            expanding, \
                                            expanding.totalCost + cost, \
                                            problem.heuristic(final_state))
                heapq.heappush(frontier, child_node)

        # No solutions found
        return None


class PathfinderTests(unittest.TestCase):
    def test_maze1(self):
        maze = ["XXXXX", "X..GX", "X...X", "X*..X", "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)

    def test_maze2(self):
        maze = ["XXXXX", "XG..X", "XX..X", "X*..X", "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)

    def test_maze3(self):
        maze = ["XXXXX", "X..GX", "X.MMX", "X*..X", "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)

    def test_maze4(self):
        maze = ["XXXXXX", "X....X", "X*.XXX", "X..XGX", "XXXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        self.assertFalse(soln)


if __name__ == '__main__':
    unittest.main()
