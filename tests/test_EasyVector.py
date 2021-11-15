import math
from unittest import TestCase

from easyvector.EasyVector import EasyVector2D


class TestEasyVector2D(TestCase):
    def test_normalize(self):
        test_vec = EasyVector2D(2, 2)
        self.assertEqual(EasyVector2D(1 / math.sqrt(2), 1 / math.sqrt(2)), test_vec.normalize)

    def test_extend(self):
        test_vec = EasyVector2D(2, 4)
        test_vec.extend(10)
        test_vec2 = EasyVector2D(20, 40)
        self.assertEqual(test_vec2, test_vec)

    def test_magnitude(self):
        test_vec = EasyVector2D(6, 0)
        test_vec2 = EasyVector2D(1, 1)
        self.assertEqual(6, test_vec.magnitude)
        self.assertAlmostEqual(math.sqrt(2), test_vec2.magnitude)

    def test_distance(self):
        test_vec = EasyVector2D(0, 0)
        test_vec2 = EasyVector2D(6, 0)
        self.assertEqual(6, test_vec.distance(test_vec2))

    def test_determinant(self):
        test_vec = EasyVector2D(2, 3)
        test_vec2 = EasyVector2D(1, 5)
        self.assertEqual(-7, test_vec.determinant(test_vec2))

    def test_angle(self):
        test_vec = EasyVector2D(0, 1)
        self.assertEqual(90, test_vec.angle())
        test_vec = EasyVector2D(1, 0)
        self.assertEqual(0, test_vec.angle())
        test_vec = EasyVector2D(0, -1)
        self.assertEqual(-90, test_vec.angle())
        test_vec = EasyVector2D(-1, 0)
        self.assertEqual(180, test_vec.angle())
        test_vec = EasyVector2D(-1, 0)
        test_vec2 = EasyVector2D(0, 1)
        self.assertEqual(90, test_vec.angle(test_vec2))
        test_vec = EasyVector2D(0, 1)
        test_vec2 = EasyVector2D(0, -1)
        self.assertEqual(180, test_vec.angle(test_vec2))

    def test_iter(self):
        test_vec = EasyVector2D(2, 4)
        self.assertEqual([2, 4], list(test_vec))

    def test_getitem(self):
        test_vec = EasyVector2D(7, 3)
        self.assertEqual(3, test_vec[1])
        self.assertEqual(7, test_vec[0])
