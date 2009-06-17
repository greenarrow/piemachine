import unittest
import piemachine



class Axis(unittest.TestCase):
	"""Test Axis"""
	
	def test_create(self):
		"""create axis object"""
		
		axis_test = piemachine.Axis(parent=None)
		
	
	def test_no_output(self):
		"""check for exception raised with output not configured"""
		
		axis_test = piemachine.Axis( parent=piemachine.Machine() )
		self.assertRaises(piemachine.PieMachineError, axis_test.seek)


class Cartesian(unittest.TestCase):
	"""Test Cartesian"""
	
	def test_create(self):
		"""create cartesian object"""
		
		class CartesianTest(piemachine.Cartesian):
			pass
		
		cartesian_test = CartesianTest( parent=piemachine.Machine() )
		
		self.assert_( issubclass(cartesian_test.__class__, piemachine.Cartesian) )
		
		cartesian_test.pre_config()
		self.assert_( issubclass(cartesian_test.machine.__class__, piemachine.Machine) )
	
	
	def test_no_machine(self):
		"""check for error when no machine is attached"""
		
		cartesian_test = piemachine.Cartesian(parent=None)
		
		self.assertRaises(piemachine.PieMachineError, cartesian_test.pre_config)


class FullCartesianStack(unittest.TestCase):
	"""Test all carteian components (machine, cartesian, axis)"""
	
		
	def test_create(self):
		"""create machine, cartesian, axis stack"""
		
		class CartesianTest(piemachine.Cartesian):
			
			def __init__(self, *args, **kwargs):
				
				piemachine.Cartesian.__init__(self, *args, **kwargs)
				
				self.x = piemachine.Axis(self)
				self.y = piemachine.Axis(self)
				self.z = piemachine.Axis(self)
		
		cartesian_test = CartesianTest( parent=piemachine.Machine() )
		
		self.assert_( issubclass(cartesian_test.__class__, piemachine.Cartesian) )
		
		cartesian_test.pre_config()
		self.assert_( issubclass(cartesian_test.machine.__class__, piemachine.Machine) )
		
		cartesian_test.x.pre_config()
		self.assert_( issubclass(cartesian_test.x.machine.__class__, piemachine.Machine) )
		
		cartesian_test.y.pre_config()
		self.assert_( issubclass(cartesian_test.y.machine.__class__, piemachine.Machine) )
		
		cartesian_test.z.pre_config()
		self.assert_( issubclass(cartesian_test.z.machine.__class__, piemachine.Machine) )
		
	
	def test_no_machine(self):
		"""check for error when no machine"""
		
		class CartesianTest(piemachine.Cartesian):
			
			def __init__(self, *args, **kwargs):
				
				piemachine.Cartesian.__init__(self, *args, **kwargs)
				
				self.x = piemachine.Axis(self)
				self.y = piemachine.Axis(self)
				self.z = piemachine.Axis(self)
		
		cartesian_test = CartesianTest( parent=None )
		
		self.assert_( issubclass(cartesian_test.__class__, piemachine.Cartesian) )
		
		self.assertRaises(piemachine.PieMachineError, cartesian_test.pre_config)
		self.assertRaises(piemachine.PieMachineError, cartesian_test.x.pre_config)
		self.assertRaises(piemachine.PieMachineError, cartesian_test.y.pre_config)
		self.assertRaises(piemachine.PieMachineError, cartesian_test.z.pre_config)



def suite():
	axis = unittest.TestLoader().loadTestsFromTestCase(Axis)
	cartesian = unittest.TestLoader().loadTestsFromTestCase(Cartesian)
	stack = unittest.TestLoader().loadTestsFromTestCase(FullCartesianStack)
	return unittest.TestSuite( [axis, cartesian, stack] )



#suite = unittest.TestLoader().loadTestsFromTestCase(unittest.TestCase)

"""
def suite():
	suite = unittest.TestSuite()
	suite.addTest( TestAxis() )
	suite.addTest( TestCartesian() )
	suite.addTest( TestFullCartesianStack() )
	return suite

"""


#self.assertEqual( f.filename, "testname" )
#self.assertEqual( f.ints, (1, 2, 3, 4) )

# Test exceptions
#self.assertRaises(TypeError, unall.get_file_sets)
#self.assert_(element in self.seq)



