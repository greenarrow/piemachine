import piemachine
import piemachine.outputs.serial_snap
import piemachine.toolheads.plastic_extruder

"""Pre-baked piemachine configurations allow for quick use of common configurations."""

class _SnapRepRapCartesianBot(piemachine.Cartesian):
	
	def __init__(self, *args, **kwargs):
		
		piemachine.Cartesian.__init__(self, *args, **kwargs)
	
		self.x = piemachine.Axis(self)
		self.y = piemachine.Axis(self)
		self.z = piemachine.Axis(self)
		
		self.x.configure_output(address=10)
		self.y.configure_output(address=11)
		self.z.configure_output(address=12)


class SnapRepRap(piemachine.Machine):
	"""Serial SNAP RepRap machine for generation 1 PIC electronics."""
	
	output = piemachine.outputs.serial_snap
	
	def __init__(self, serial_port, *args, **kwargs):
		
		piemachine.Machine.__init__(self, *args, **kwargs)
		
		self.cartesian = _SnapRepRapCartesianBot(self)
		
		self.extruder = piemachine.toolheads.plastic_extruder.Tool(self)
		self.extruder.configure_output(address=13)
		
		self.configure_output(serial_port=serial_port)

