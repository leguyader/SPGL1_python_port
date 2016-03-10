# -*- coding: utf-8 -*-
""" SPGL1 tests.

Copyright (2016) Loïc Le Guyader <loic.le.guyader@xfel.eu>
"""

import unittest
 
class TestSPGL1(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_spgSetParms(self):
        """ Testing spgSetParms behavior """
        import spgl_aux
        m = 20
        options = spgl_aux.spgSetParms({'iterations':10*m})
        self.assertEqual(10*m, options['iterations']), "Default iteration as in spgl1 not set properly"
        options2 = spgl_aux.spgSetParms({'rootMethod':-1}, options)
        options3 = spgl_aux.spgSetParms({'verbosity':0}, options2)
        self.assertEqual(-1, options3['rootMethod']), "Parameters get erased upon calling spgSetParms"
 
if __name__ == '__main__':
    unittest.main()
