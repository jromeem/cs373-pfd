# Jerome Martinez
# Michael Pace
# C S 373
# TestPFD.py

# -------
# imports
# -------

import StringIO
import unittest

from PFD import pfd_read, pfd_eval, pfd_print, pfd_solve, build_pred, build_succ

class TestPFD (unittest.TestCase) :

    # -------------
    # test pfd_read
    # -------------
    def test_read_1 (self) :
        r = StringIO.StringIO("1 10\n")
        tk, rl = pfd_read(r)
        self.assert_(tk ==  1)
        self.assert_(rl == 10)
    def test_read_2 (self):
        r = StringIO.StringIO("5 4\n")
        tk, rl = pfd_read(r)
        self.assert_(tk ==  5)
        self.assert_(rl == 4)
    def test_read_3 (self):
        r = StringIO.StringIO("8721 2983798\n")
        tk, rl = pfd_read(r)
        self.assert_(tk ==  8721)
        self.assert_(rl == 2983798)

    # -------------
    # test pfd_eval
    # -------------
    def test_eval_1 (self):
        p = [[], [], [5, 3], [1, 5], [3], [1]]
        s = [[], [3, 5], [], [2, 4], [], [2, 3]]
        out = pfd_eval(p, s)
        self.assert_(out ==  ['1', ' ', '5', ' ', '3', ' ', '2', ' ', '4'])
    def test_eval_2 (self):
        p = [[], [], [1], [2]]
        s = [[], [2], [3], []]
        out = pfd_eval(p, s)
        self.assert_(out ==  ['1', ' ', '2', ' ', '3'])
    def test_eval_3 (self):
        p = [[], [], [1], [], [3, 1, 2], [4]]
        s = [[], [2, 4], [4], [4], [5], []]
        out = pfd_eval(p, s)
        self.assert_(out ==  ['1', ' ', '2', ' ', '3', ' ', '4', ' ', '5'])

    # --------------
    # test pfd_print
    # --------------
    def test_print_1 (self):
        w = StringIO.StringIO()
        pfd_print(w, ['2', '3', ' ', ' ', 'hello'])
        self.assert_(w.getvalue() == "23  hello")
    def test_print_2 (self):
        w = StringIO.StringIO()
        pfd_print(w, ['1', '2', '3', ' '])
        self.assert_(w.getvalue() == "123 ")
    def test_print_3 (self):
        w = StringIO.StringIO()
        pfd_print(w, [])
        self.assert_(w.getvalue() == "")

    # --------------
    # test pfd_solve
    # --------------
    def test_solve_1 (self):
        r = StringIO.StringIO("5 4\n3 2 1 5\n2 2 5 3\n4 1 3\n5 1 1\n")
        w = StringIO.StringIO()
        pfd_solve(r, w)
        self.assert_(w.getvalue() == "1 5 3 2 4")
    def test_solve_2 (self):
        r = StringIO.StringIO("3 2\n2 1 1\n3 1 2")
        w = StringIO.StringIO()
        pfd_solve(r, w)
        self.assert_(w.getvalue() == "1 2 3")
    def test_solve_3 (self):
        r = StringIO.StringIO("5 3\n2 1 1\n4 3 3 1 2\n5 1 4\n")
        w = StringIO.StringIO()
        pfd_solve(r, w)
        self.assert_(w.getvalue() == "1 2 3 4 5")

    # ---------------
    # test build_pred
    # ---------------
    def test_build_pred_1 (self):
        r = StringIO.StringIO("3 2 1 5\n2 2 5 3\n4 1 3\n5 1 1\n")
        tk = 5
        rl = 4
        out = build_pred(r, tk, rl)
        self.assert_(out == [[], [], [5, 3], [1, 5], [3], [1]])
    def test_build_pred_2 (self):
        r = StringIO.StringIO("2 1 1\n3 1 2\n")
        tk = 3
        rl = 2
        out = build_pred(r, tk, rl)
        self.assert_(out == [[], [], [1], [2]])
    def test_build_pred_3 (self):
        r = StringIO.StringIO("2 1 1\n4 3 3 1 2\n5 1 4\n")
        tk = 5
        rl = 3
        out = build_pred(r, tk, rl)
        self.assert_(out == [[], [], [1], [], [3, 1, 2], [4]])

    # ---------------
    # test build_succ
    # ---------------
    def test_build_succ_1 (self):
        s = [[], [], [5, 3], [1, 5], [3], [1]]
        out = build_succ(s)
        self.assert_(out == [[], [3, 5], [], [2, 4], [], [2, 3]])
    def test_build_succ_2 (self):
        s = [[], [], [1], [2]]
        out = build_succ(s)
        self.assert_(out == [[], [2], [3], []])
    def test_build_succ_3 (self):
        s = [[], [], [1], [], [3, 1, 2], [4]]
        out = build_succ(s)
        self.assert_(out == [[], [2, 4], [4], [4], [5], []])

# ----
# main
# ----
print "TestPFD.py"
unittest.main()
print "Done."
