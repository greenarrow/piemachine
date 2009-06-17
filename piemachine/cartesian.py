import piemachine

#TODO create decorators for veritying different types of variable (int, float, 0-255 etc).

#TODO add a require_parent_cartesian decorator to restrict some functions to cartesian parented axes only? do we need to?


class Axis:
	output_configured = False
	machine = None
	position = None
	# TODO - make a property that allows switching between working with (returned) dicts, tuples, or simple lists (e.g. for axis positions)
	
	def __init__(self, parent):
		self.parent = parent
	
	
	@piemachine.require_machine
	
	def configure_output(self, *args, **kwargs):
		self.output_object = self.machine.output.Axis(self)
		self.output_configured = self.output_object.configure(*args, **kwargs)
	
	
	@piemachine.require_machine
	
	def pre_config(self):
		# just to manually run @piemachine.require_machine
		pass
	
	
	@piemachine.require_machine
	@piemachine.require_configured_output
	
	def get_position(self):
		#print "move", value
		print "this function has not been implemented"
		#TODO do we really want to store it here? or just pass to plugin to worry about :)
		return self.position
	
	
	@piemachine.require_machine
	@piemachine.require_configured_output
	
	def set_position(self, value):
		print "set position", value
		#TODO do we really want to store it here? or just pass to plugin to worry about :)
		self.position = value
		print "this function has not been implemented"
	
	@piemachine.require_machine
	@piemachine.require_configured_output
	
	def move(self, value):
		print "move", value
		print "this function has not been implemented"
	

	
	@piemachine.require_machine
	@piemachine.require_configured_output
	
	def seek(self, value):
		print "seek", value
		print "this function has not been implemented"





class Cartesian:
	axes = None
		
	def __init__(self, parent):
		self.parent = parent	
	
	@piemachine.require_machine
	def pre_config(self):
		# just to manually run @piemachine.require_machine
		pass
		
	def _dda(self):
		print "this function has not been implemented"
	
	def make_axes_list(self):
		self.axes = {}
		for name in dir(self):
			item = getattr(self, name)
			if issubclass( item.__class__, piemachine.Axis):
				self.axes[name] = item
				print name
		print self.axes
	
	@piemachine.require_machine
	@piemachine.require_axes_list
	
	def seek(self):
		print "this function has not been implemented"
	

"""
TODO
in piemachine cartesian seek / dda function:
1. look at the parameters:
	if there is just one axis then just direct command to that axis.
	we are done.
	
2. if there is more than one then enter dda mode.
3. look at all the axes, decide which has greatest movement.
4. call dda function on master axis, passing it the master axis' destination, and a tuple of the other axes and destinations. e.g. ( (AxisObjectX, 20), (AxisObjectZ, 10) )
	the master axis (in plugin) is responsible for configuring the other two throught their .output_object(s)
	In a plugin that does not do real machine control, this can easily be converted back into a nice cartesian coordinate.


idea - share the dda function between move and seek
	
"""

	
	@piemachine.require_machine
	@piemachine.require_axes_list
	
	def move(self):
		print "this function has not been implemented"
	
	
	@piemachine.require_machine
	@piemachine.require_axes_list
	
	def get_position(self):
		result = {}
		for name, axis in self.axes.iteritems():
			result[name] = axis.get_position()
		return result
	
	
	@piemachine.require_machine
	@piemachine.require_axes_list
	
	def set_position(self, *args, **kwargs):
		print "this function has not been implemented"
		



"""
	def add_axis(self, name, axis):
		axis.parent = self
		self.axes[name] = axis
		# TODO - raise exception if already in table
		setattr( self, name, axis )
	
		
	def setup_axes_xyz(self):
		self.add_axis( 'x', Axis() )
		self.add_axis( 'y', Axis() )
		self.add_axis( 'z', Axis() )
"""










