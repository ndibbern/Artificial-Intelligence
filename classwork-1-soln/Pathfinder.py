'''
The Pathfinder class is responsible for finding a solution (i.e., a
sequence of actions) that takes the agent from the initial state to the
optimal goal state.

This task is done in the Pathfinder.solve method, as parameterized
by a maze pathfinding problem, and is aided by the SearchTreeNode DS.
'''

from MazeProblem import MazeProblem
from SearchTreeNode import SearchTreeNode
import queue
import unittest

class Pathfinder:

    def getSolution(node):
        soln = []
        while node.parent is not None:
            soln.append(node.action)
            node = node.parent
        soln.reverse()
        return soln

    def solve(problem):
        # Setup
        frontier = queue.Queue()
        node_count = 0

        # Search!
        frontier.put(SearchTreeNode(problem.initial, None, None))
        while not frontier.empty():
            # Get front of queue
            expanding = frontier.get()

            # Test for goal state
            if problem.goalTest(expanding.state):
                print(node_count)
                return Pathfinder.getSolution(expanding)

            # Generate new nodes on frontier
            for child in problem.transitions(expanding.state):
                frontier.put(SearchTreeNode(child[1], child[0], expanding))
                node_count += 1

        # Should never get here if solution (guaranteed for this classwork)
        return []

class PathfinderTests(unittest.TestCase):
    def test_maze1(self):
        maze = ["XXXXX", "X..GX", "X...X", "X*..X", "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)

    # def test_maze2(self):
    #     maze = ["XXXXX", "XG..X", "XX..X", "X*..X", "XXXXX"]
    #     problem = MazeProblem(maze)
    #     soln = Pathfinder.solve(problem)
    #     solnTest = problem.solnTest(soln)
    #     self.assertTrue(solnTest[1])
    #     self.assertEqual(solnTest[0], 4)
    #
    # def test_maze3(self):
    #     maze = ["XXXXX", "XG..X", "XX..X", "X*.GX", "XXXXX"]
    #     problem = MazeProblem(maze)
    #     soln = Pathfinder.solve(problem)
    #     solnTest = problem.solnTest(soln)
    #     self.assertTrue(solnTest[1])
    #     self.assertEqual(solnTest[0], 2)
    #
    # def test_maze4(self):
    #     # Breaking up big mazes, for clarity
    #     maze = ["XXXXXXX",\
    #             "X..*..X",\
    #             "XXX.XXX",\
    #             "X.....X",\
    #             "X.X.XGX",\
    #             "XXXXXXX"]
    #     problem = MazeProblem(maze)
    #     soln = Pathfinder.solve(problem)
    #     solnTest = problem.solnTest(soln)
    #     self.assertTrue(solnTest[1])
    #     self.assertEqual(solnTest[0], 5)
    #
    # def test_maze5(self):
    #     maze = ["XXXXXXX",\
    #             "X..*..X",\
    #             "XXX.XXX",\
    #             "XG....X",\
    #             "X.X.XGX",\
    #             "XXXXXXX"]
    #     problem = MazeProblem(maze)
    #     soln = Pathfinder.solve(problem)
    #     solnTest = problem.solnTest(soln)
    #     self.assertTrue(solnTest[1])
    #     self.assertEqual(solnTest[0], 4)
    #
    # def test_maze6(self):
    #     maze = ["XXXXXXX",\
    #             "XGX...X",\
    #             "XXX...X",\
    #             "X..*..X",\
    #             "X.....X",\
    #             "X....GX",\
    #             "XXXXXXX"]
    #     problem = MazeProblem(maze)
    #     soln = Pathfinder.solve(problem)
    #     solnTest = problem.solnTest(soln)
    #     self.assertTrue(solnTest[1])
    #     self.assertEqual(solnTest[0], 4)
    #
    # def test_maze7(self):
    #     maze = ["XXXXXXX",\
    #             "X..G..X",\
    #             "X.....X",\
    #             "X.G*.GX",\
    #             "X.....X",\
    #             "X..G..X",\
    #             "XXXXXXX"]
    #     problem = MazeProblem(maze)
    #     soln = Pathfinder.solve(problem)
    #     solnTest = problem.solnTest(soln)
    #     self.assertTrue(solnTest[1])
    #     self.assertEqual(solnTest[0], 1)
    #
    # def test_maze8(self):
    #     maze = ["XXXXXXX",\
    #             "X*....X",\
    #             "XXXXX.X",\
    #             "X.....X",\
    #             "X.XXXXX",\
    #             "X....GX",\
    #             "XXXXXXX"]
    #     problem = MazeProblem(maze)
    #     soln = Pathfinder.solve(problem)
    #     solnTest = problem.solnTest(soln)
    #     self.assertTrue(solnTest[1])
    #     self.assertEqual(solnTest[0], 16)

    def test_maze5(self):
        maze = ["XXXXXXXXXXXX",\
                "XG.......XGX",\
                "X...XXX..X.X",\
                "X...XGX..X.X",\
                "X...XXX..X.X",\
                "X.......XX.X",\
                "X..........X",\
                "X......XXXXX",\
                "X.........*X",\
                "XXXXXXXXXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        soln_test = problem.solnTest(soln)
        self.assertTrue(soln_test[1])
        self.assertEqual(soln_test[0], 15)

if __name__ == '__main__':
    unittest.main()
