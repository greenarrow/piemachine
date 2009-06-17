#!/usr/bin/env python

import unittest, os, time

import reprap2, reprap2.outputs.serial_snap



class TestCartesian(unittest.TestCase):
	"""Test Catresian"""
	
	def test_create(self):
		"""Test create"""
		
		def make():
			c = reprap2.Cartesian( output=reprap2.outputs.serial_snap, axes=4 )
		
		self.assertRaises(reprap2._RepRapError, make )
		
	def test_check_axies(self):
		"""Test axies"""
		
		c = reprap2.Cartesian( output=reprap2.outputs.serial_snap, axes=3 )
		
		self.assert_( 'x' in dir(c) )
		self.assert_( 'y' in dir(c) )
		self.assert_( 'z' in dir(c) )
		
		
		#self.assertEqual( f.filename, "testname" )
		#self.assertEqual( f.ints, (1, 2, 3, 4) )
		
		# Test exceptions
		#self.assertRaises(TypeError, unall.get_file_sets)
		#self.assert_(element in self.seq)



unittest.main()
