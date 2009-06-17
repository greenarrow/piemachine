class Machine:
	
	def __init__(self, *args, **kwargs):
		pass
		
	def configure_output(self, *args, **kwargs):
		self.output_object = self.output.Machine(self)
		self.output_configured = self.output_object.configure(*args, **kwargs)
	

