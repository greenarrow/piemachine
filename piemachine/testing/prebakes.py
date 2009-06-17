import unittest
import piemachine

import piemachine.prebaked



class Prebakes(unittest.TestCase):
	"""Test pre-baked piemachine configs"""
	
	def test_SnapRepRap(self):
		"""create RepRap pre-bake"""
		
		machine_test = piemachine.prebaked.SnapRepRap(serial_port=None)
		self.assert_( issubclass(machine_test.__class__, piemachine.Machine) )


def suite():
	return unittest.TestLoader().loadTestsFromTestCase(Prebakes)

"""
def suite():
	suite = unittest.TestSuite()
	suite.addTest( TestPrebakes() )
	return suite
"""






