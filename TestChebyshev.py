import unittest

from Chebyshev import Chebyshev

class TestChebyshev(unittest.TestCase):

    def test_Chebyshev(self):
        c = Chebyshev(6)
        self.assertEqual([-1, 0, 18, 0, -48, 0, 32], c.coefficients)

if __name__ == '__main__':
        unittest.main()