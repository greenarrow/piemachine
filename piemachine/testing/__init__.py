import os, glob

"""
def get_suites():
	old_dir = os.getcwd()
	
	testsuite_path = os.path.split(__file__)[0]
	print testsuite_path
	os.chdir(testsuite_path)
	print os.getcwd()
	suites = []	
	
	for filename in glob.glob('*.py'):
		if filename != '__init__.py':
			print filename
			module = __import__( filename )
			suites.append( module.suite )
	
	os.chdir(old_dir)
	
	return suites
"""



def get_suites():
	
	import machine, cartesian, prebakes
	
	return [ machine.suite(), cartesian.suite(), prebakes.suite() ]
