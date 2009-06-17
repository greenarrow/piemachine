
"""
import os

debug = True

plugins = {}
plugins_path = os.path.split(__file__)[0]

for f in os.listdir(plugins_path):
	
	if os.path.isdir( os.path.join(plugins_path, f) ) and '__init__.py' in os.listdir( os.path.join(plugins_path, f) ):
		
		if debug:
			print 'importing plugin %s' % f
		plugins[f] = __import__( os.path.join(plugins_path, f) )
		
"""
