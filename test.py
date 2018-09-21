#/usr/bin/env python

import unittest

from assignment7 import *

class TestSolution(unittest.TestCase):

    def test_fit(self):

	    kc = KozenyCarmen('poro_perm.dat')
	    
	    kc.fit()
	    
	    np.testing.assert_allclose(kc.fit(), np.array([  1.05933127e+01,   2.35173520e+04]), atol=0.001)
    
    def test_fit_through_zero(self):

	    kc = KozenyCarmen('poro_perm.dat')

	    kc.fit_through_zero()
	    
	    np.testing.assert_allclose(kc.fit_through_zero(),26133.929742741482, atol=0.001)


if __name__ == '__main__':
    unittest.main()
