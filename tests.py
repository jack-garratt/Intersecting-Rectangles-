from main import define_corners, compare_sides
import unittest

class test_define_corners(unittest.TestCase):
    def test_all_positive(self):
        self.assertEqual(define_corners(0,10,10,0),([[0,10],[10,10],[0,0],[10,0]]))
    def test_negative_coordinates(self):
        self.assertEqual(define_corners(-20,-10,-10,-20), ([[-20,-10],[-10,-10],[-20,-20],[-10,-20]]))
    def test_around_origin(self):
        self.assertEqual(define_corners(-5,5,5,-5), ([[-5,5],[5,5],[-5,-5],[5,-5]]))
    def test_x_equal(self):
        self.assertFalse(define_corners(5,10,5,0))
    def test_y_equal(self):
        self.assertFalse(define_corners(0,5,10,5))
    def test_all_equal(self):
        self.assertFalse(define_corners(5,10,5,10))
    def test_x2_less_x1(self):
        self.assertFalse(define_corners(10,10,5,0))
    def test_y2_greater_y1(self):
        self.assertFalse(define_corners(0,0,10,5))

class test_compare_sides(unittest.TestCase):
    def test_identical_rectangles(self):
        self.assertTrue(compare_sides([[[0,10],[10,10],[0,0],[10,0]],[[0,10],[10,10],[0,0],[10,0]]]))
    def test_left_overlap(self): 
        self.assertTrue(compare_sides([[[-5,5],[5,5],[-5,-5],[5,-5]],[[-10,5],[0,5],[-10,-5],[0,-5]]]))
    def test_right_overlap(self): 
        self.assertTrue(compare_sides([[[-5,5],[5,5],[-5,-5],[5,-5]],[[0,5],[10,5],[0,-5],[10,-5]]]))
    def test_top_overlap(self): 
        self.assertTrue(compare_sides([[[-5,5],[5,5],[-5,-5],[5,-5]],[[-5,10],[5,10],[-5,0],[5,0]]]))
    def test_bottom_overlap(self):
        self.assertTrue(compare_sides([[[-5,5],[5,5],[-5,-5],[5,-5]],[[-5,0],[5,5],[-5,-10],[5,-10]]]))
    def test_non_left(self):
        self.assertFalse(compare_sides([[[-10,5],[0,5],[-10,-5],[0,-5]],[[0,5],[10,5],[0,-5],[10,-5]]]))
    def test_non_left(self):
        self.assertFalse(compare_sides([[[10,5],[20,5],[10,-5],[20,-5]],[[0,5],[10,5],[0,-5],[10,-5]]]))
    def test_non_top(self):
        self.assertFalse(compare_sides([[[0,5],[10,5],[0,-5],[10,-5]],[[0,15],[10,15],[0,5],[10,5]]]))
    def test_non_top_right(self):
        self.assertFalse(compare_sides([[[0,5],[10,5],[0,-5],[10,-5]],[[10,15],[20,15],[10,5],[20,5]]]))
    def test_intercecting_no_points(self):
        self.assertTrue(compare_sides([[[-10,5],[10,5],[-10,-5],[10,-5]],[[-5,10],[5,10],[-5,-10],[5,-10]]]))

if __name__ == "__main__":
    unittest.main()