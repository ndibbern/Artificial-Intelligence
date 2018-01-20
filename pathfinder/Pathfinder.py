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

class Pathfinder:

    # solve is parameterized by a maze pathfinding problem
    # (see MazeProblem.py and unit tests below), and will
    # return a list of actions that solves that problem. An
    # example returned list might look like:
    # ["U", "R", "R", "U"]
    def solve(problem):
        current_node = SearchTreeNode(problem.initial, None, None)
        q = [current_node]
        while not problem.goal_test(current_node.state):
            current_node = q.pop(0)
            children = problem.transitions(current_node.state)
            for child in children:
                child_action, child_state = child
                child_node = SearchTreeNode(child_state, child_action, current_node)
                q.append(child_node)

        path = []
        while current_node.parent != None:
            path.append(current_node.action)
            current_node = current_node.parent

        return list(reversed(path))


class PathfinderTests(unittest.TestCase):
    def test_maze1(self):
        maze = ["XXXXX", "X..GX", "X...X", "X*..X", "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        soln_test = problem.soln_test(soln)
        self.assertTrue(soln_test[1])
        self.assertEqual(soln_test[0], 4)

    def test_maze2(self):
        maze = ["XXXXX", \
                "XG..X", \
                "XX..X", \
                "X*..X", \
                "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        soln_test = problem.soln_test(soln)
        self.assertTrue(soln_test[1])
        self.assertEqual(soln_test[0], 4)

    # TODO: Add more unit tests!

if __name__ == '__main__':
    unittest.main()
    # maze = ["XXXXX", \
    #         "XG..X", \
    #         "XX..X", \
    #         "X*..X", \
    #         "XXXXX"]
    # problem = MazeProblem(maze)
    # print("Initial: ", problem.initial)
    # print("Goal: ", problem.goals)
    # print(Pathfinder.solve(problem))
