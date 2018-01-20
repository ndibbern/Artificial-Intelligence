'''
MazeProblem Formalization:
MazeProblems represent 2D pathfinding problems, as programmatically
formalized via:

=== Mazes ===
Represented as a list of strings in which:
  X = impassable wall
  * = the initial state
  . = open cells
  G = goal states
All valid mazes have:
  - At most 1 initial state
  - At least 1 goal state
  - A border of walls (plus possibly other walls)
  - A solution
(We'll ignore invalid maze states as possible inputs, for simplicity)

Maze elements are indexed starting at (0, 0) [top left of maze]. E.g.,
["XXXXX", "X..GX", "X...X", "X*..X", "XXXXX"] is interpretable as:
  01234 first
0 XXXXX
1 X..GX
2 X...X
3 X*..X
4 XXXXX
last

=== States ===
Representing the position of the agent, as tuples in which:
(x, y) = (col, row)
(0, 0) is located at the top left corner; Right is +x, and Down is +y

=== Actions ===
Representing the allowable Up, Down, Left, and Right movement capabilities
of the agent in the 2D Maze; we'll simply use string representations:
"U", "D", "L", "R"

=== Transitions ===
Given some state s, the transitions will be represented as a list of tuples
of the format:
[(action1, result(action1, s)), ...]
For example, if an agent is at state (1, 1), and can only move right and down,
then the transitions for that s = (1, 1) would be:
[("R", (2, 1)), ("D", (1, 2))]

'''
import re
import numpy as np

class MazeProblem:

    def __init__(self, maze):
        self.actions = {"U":(0, -1) , "D":(0, 1), "L":(-1, 0), "R":(1, 0)}
        self.maze = maze
        self.initial = self.where('*').pop()
        self.goals = self.where('G')

    def where(self, char):
        result = set()
        for row in range(len(self.maze)):
            for col in range(len(self.maze[row])):
                if self.maze[row][col] == char:
                    result.add((col, row))
        return result

    def goal_test(self, state):
        return state in self.goals

    # [('R', (3, 4)), ('L', (2, 3))]
    def transitions(self, state):
        x, y = state
        transitions = []
        for action, delta in self.actions.items():
            dx, dy = delta
            result = (x+dx, y+dy)
            if self.valid(result):
                transitions.append((action, result))
        return transitions

    def valid(self, state):
        x, y = state
        try:
            return self.maze[y][x] != 'X'
        except:
            return False

    # solnTest will return a tuple of the format (cost, isSoln) where:
    # cost = the total cost of the solution,
    # isSoln = true if the given sequence of actions of the format:
    # [a1, a2, ...] successfully navigates to a goal state from the initial state
    # If NOT a solution, return a cost of -1
    def soln_test(self, soln):
        trans = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
        s = self.initial
        for m in soln:
            s = (s[0] + trans[m][0], s[1] + trans[m][1])
            if self.maze[s[1]][s[0]] == "X":
                return (-1, False)
        return (len(soln), self.goal_test(s))

if __name__ == '__main__':
    problem = MazeProblem(\
        [ "XXXXX"\
        , "XG.GX"\
        , "XX..X"\
        , "X*..X"\
        , "XXXXX" ])
    print("Initial: ", problem.initial)
    print("Goal: ", problem.goals)
    print(problem.transitions((1,3)))
