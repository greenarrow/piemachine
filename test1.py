#!/usr/bin/env python

import piemachine

import piemachine.outputs.serial_snap
import piemachine.toolheads.plastic_extruder



class CartesianBot(piemachine.Cartesian):
	
	def __init__(self, *args, **kwargs):
		
		piemachine.Cartesian.__init__(self, *args, **kwargs)
	
		self.x = piemachine.Axis(self)
		self.y = piemachine.Axis(self)
		self.z = piemachine.Axis(self)
		
		self.x.configure_output(address=10)
		self.y.configure_output(address=11)
		self.z.configure_output(address=12)


class RepRap(piemachine.Machine):
	
	output = piemachine.outputs.serial_snap
	
	def __init__(self, *args, **kwargs):
		
		piemachine.Machine.__init__(self, *args, **kwargs)
		
		self.cartesian = CartesianBot(self)
		
		self.extruder = piemachine.toolheads.plastic_extruder.Tool(self)
		self.extruder.configure_output(address=13)
		
		self.configure_output(serial_port='/dev/ttyUSB0')
	
	

rep = RepRap()


print rep.cartesian.get_position()

rep.cartesian.x.seek(100)

# idea - make code that generates wx panel from a list of variables. uses widgets apropriate to type, and does text back to type conversions automatically
# plugins can then have this simple list rather than needed a wx panel designed manually for each one.








"""
m = piemachine.Machine(output=piemachine.outputs.serial_snap)

c = piemachine.cartesian.Cartesian()

# configure the axes manually:

x = piemachine.cartesian.Axis()
c.add_axis('x', x)
y = piemachine.cartesian.Axis()
c.add_axis('y', y)
z = piemachine.cartesian.Axis()
c.add_axis('z', z)

# or set up x, y, z automatically with default settings:
#c.setup_axes_xyz()

m.add_component(c)

e = piemachine.toolheads.plastic_extruder.PlasticExtruder()

m.add_component(e)


c.move()

"""





"""
wx guidelines:

app = wx.App()
window = wx.Frame(None, style=wx.MAXIMIZE_BOX | wx.RESIZE_BORDER 
	| wx.SYSTEM_MENU | wx.CAPTION |	 wx.CLOSE_BOX)
window.Show(True)

app.MainLoop()



import wx

class Size(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(250, 200))

        self.Show(True)


app = wx.App()
Size(None, -1, 'Size')
app.MainLoop()



"""




"""
class Machine:
	
	def __init__(self):
		
		#self.cartesian = piemachine.Cartesian(output='serial-snap')
		self.cartesian = piemachine.Cartesian( output=piemachine.outputs.serial_snap, axies=('x', 'y', 'z') )
		#self.extruder = 


m = Machine()

m.cartesian.move()
"""




