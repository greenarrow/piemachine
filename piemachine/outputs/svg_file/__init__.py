__title__ = 'svg file'

class Machine:
	
	def __init__(self, parent, *args, **kwargs):
		self.parent = parent
	
	config_optional = []
	config_required = ['filename']
	
	def configure(self, *args, **kwargs):	
		if 'filename' in kwargs:
			self.filename = kwargs['filename']
			print "%s machine has filename %s" % (__title__, self.filename)
			return True
		else:
			return False


class Axis:
	def __init__(self, parent, *args, **kwargs):
		self.parent = parent


#class Machine:
#	pass
