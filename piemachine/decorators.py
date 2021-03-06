import piemachine

"""Decorator to check if object has a machine assigned, and locate it up parent tree if not"""
def require_machine(func):
	def new_func(obj, *args, **kwargs):
		
		if not 'machine' in dir(obj) or not issubclass(obj.machine.__class__, piemachine.Machine):
			part = obj
			
			while 'parent' in dir(part):
				part = part.parent
			
				if issubclass(part.__class__, piemachine.Machine):
					obj.machine = part
					break
			
			else:
				raise piemachine.PieMachineError( "can't find machine assigned to %s" % str(obj) )
			
		return func(obj, *args, **kwargs)

	return new_func


def require_configured_output(func):
	def new_func(obj, *args, **kwargs):
		
		if not obj.output_configured:
			raise piemachine.PieMachineError( "output plugin not configured for %s" % str(obj) )
			#obj.configure_output()
			
		return func(obj, *args, **kwargs)

	return new_func

def require_axes_list(func):
	def new_func(obj, *args, **kwargs):
		
		if not obj.axes:
			obj.make_axes_list()
			
		return func(obj, *args, **kwargs)

	return new_func




