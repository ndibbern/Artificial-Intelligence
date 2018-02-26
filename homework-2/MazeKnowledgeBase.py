'''
Natalia Dibbern

MazeKnowledgeBase.py

Specifies a simple, Conjunctive Normal Form Propositional
Logic Knowledge Base for use in Grid Maze pathfinding problems
with side-information.
'''
from MazeClause import MazeClause
import unittest
from itertools import combinations

class MazeKnowledgeBase:

    def __init__(self):
        self.clauses = set()

    # [!] Assumes that a clause is never added that causes the
    # KB to become inconsistent
    def tell(self, clause):
        self.clauses.add(clause)

    # [!] Queries are always MazeClauses
    def ask(self, query):

        query_clauses = list(set(query.props.items()))
        for mazeProposition, negationStatus in query_clauses:
            self.clauses.add(MazeClause([(mazeProposition, not negationStatus)]))
        for i in self.clauses:
            print(i)
        print('-----------------------')
        new = set()
        while(True):
            pairs_iterator = combinations(self.clauses, 2)
            for ci, cj in pairs_iterator:
                resolvents = MazeClause.resolve(ci, cj)
                print('C1:')
                print(ci)
                print('C2:')
                print(cj)
                print("Resolvents:")
                if not any(resolvents): print('resolvents is empty')
                for i in resolvents:
                    print(i)
                if MazeClause([]) in resolvents:
                    return True
                new = new.union(resolvents)
                print("Printing new")
                for i in new:
                    print(i)
            if new.issubset(self.clauses): return False
            self.clauses = self.clauses.union(new)
            print("Union of clauses")
            for i in self.clauses:
                print(i)


class MazeKnowledgeBaseTests(unittest.TestCase):
    # def test_mazekb1(self):
    #     kb = MazeKnowledgeBase()
    #     kb.tell(MazeClause([(("X", (1, 1)), True)]))
    #     self.assertTrue(kb.ask(MazeClause([(("X", (1, 1)), True)])))

    def test_mazekb2(self):
        kb = MazeKnowledgeBase()
        kb.tell(MazeClause([(("X", (1, 1)), False)]))
        kb.tell(MazeClause([(("X", (1, 1)), True), (("Y", (1, 1)), True)]))
        self.assertTrue(kb.ask(MazeClause([(("Y", (1, 1)), True)])))

    # def test_mazekb3(self):
    #     kb = MazeKnowledgeBase()
    #     kb.tell(MazeClause([(("X", (1, 1)), False), (("Y", (1, 1)), True)]))
    #     kb.tell(MazeClause([(("Y", (1, 1)), False), (("Z", (1, 1)), True)]))
    #     kb.tell(MazeClause([(("W", (1, 1)), True), (("Z", (1, 1)), False)]))
    #     kb.tell(MazeClause([(("X", (1, 1)), True)]))
    #     self.assertTrue(kb.ask(MazeClause([(("W", (1, 1)), True)])))
    #     self.assertFalse(kb.ask(MazeClause([(("Y", (1, 1)), False)])))
    #
    # def test_mazekb4(self):
    #     kb = MazeKnowledgeBase()
    #     kb.tell(MazeClause([(("X", (1, 1)), False), (("Y", (1, 1)), True), (("W", (1, 1)), True)]))
    #     kb.tell(MazeClause([(("W", (1, 1)), False), (("Z", (1, 1)), False), (("S", (1, 1)), True)]))
    #     kb.tell(MazeClause([(("S", (1, 1)), False), (("T", (1, 1)), False)]))
    #     kb.tell(MazeClause([(("X", (1, 1)), True), (("T", (1, 1)), True)]))
    #     kb.tell(MazeClause([(("W", (1, 1)), True)]))
    #     kb.tell(MazeClause([(("T", (1, 1)), True)]))
    #     self.assertTrue(kb.ask(MazeClause([(("Z", (1, 1)), False)])))
    #
    # def test_mazekb5(self):
    #     kb = MazeKnowledgeBase()
    #     kb.tell(MazeClause([(("X", (1, 1)), False), (("Y", (1, 1)), True), (("W", (1, 1)), True)]))
    #     kb.tell(MazeClause([(("W", (1, 1)), False), (("Z", (1, 1)), False), (("S", (1, 1)), True)]))
    #     kb.tell(MazeClause([(("S", (1, 1)), False), (("T", (1, 1)), False)]))
    #     kb.tell(MazeClause([(("X", (1, 1)), True), (("T", (1, 1)), True)]))
    #     kb.tell(MazeClause([(("W", (1, 1)), True)]))
    #     kb.tell(MazeClause([(("T", (1, 1)), True)]))
    #     self.assertTrue(kb.ask(MazeClause([(("Z", (1, 1)), True), (("W", (1, 1)), True)])))
    #
    # def test_mazekb6(self):
    #     kb = MazeKnowledgeBase()
    #     kb.tell(MazeClause([(("X", (1, 1)), False), (("Y", (1, 1)), False), (("Z", (1, 1)), False)]))
    #     kb.tell(MazeClause([(("X", (1, 1)), True)]))
    #     self.assertFalse(kb.ask(MazeClause([(("Z", (1, 1)), False)])))
    #     kb.tell(MazeClause([(("Y", (1, 1)), True)]))
    #     self.assertTrue(kb.ask(MazeClause([(("Z", (1, 1)), False)])))


if __name__ == "__main__":
    unittest.main()
