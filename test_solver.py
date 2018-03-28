from unittest import TestCase

from solver import Solver

class TestSolver(TestCase):

    def test_negative_disc(self):
        s = Solver()
        with self.assertRaises(Exception):
            s.demo(2,1,1)

    def test_demo(self):
        s = Solver()
        l = s.demo(2,1,0)
        for elt in [0.0, -0.5]:
            self.assertIn(elt, l)


