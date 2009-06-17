#!/usr/bin/env python

import unittest
import piemachine
import piemachine.testing

#import piemachine.outputs.serial_snap
#import piemachine.toolheads.plastic_extruder

#

#print piemachine.testing.get_suites()
alltests = unittest.TestSuite( piemachine.testing.get_suites() )
#print alltests	
result = unittest.TestResult()

#print alltests.countTestCases()



#ts = piemachine.testing.get_suites()[0]
#result = unittest.TestResult()
#ts.run(result)




unittest.TextTestRunner(verbosity=2).run(alltests)

#alltests.run(result)
#unittest.main()








"""
suite = unittest.TestSuite()
suite.addTest( TestMachine() )
suite.addTest( TestAxis() )
suite.addTest( TestCartesian() )
suite.addTest( TestFullCartesianStack() )
"""


