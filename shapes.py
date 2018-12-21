# shapes.py
# VERSION 4
# Carrie Nguyen
# CS151 F18

import turtle_interpreter as it

class Shape:

	def __init__(self, distance = 100, angle = 90, color = (0, 0, 0), istring = '' ):
		''' Initializes Shape object '''
		self.distance = distance
		self.angle = angle
		self.color = color
		self.string = istring
		self.style = 'normal'
		self.jitterSigma = 2
		self.width = 1
		self.dotSize = 2
 
	def setColor(self, c):
		self.color = c
		
	def setDistance(self, d):
		self.distance = d
		
	def setAngle(self, a):
		self.angle = a
		
	def setString(self, s):
		self.string = s
	
	def setStyle(self, s):
		self.style = s
		
	def setJitter(self, j):
		self.jitterSigma = j
		
	def setWidth(self, w):
		self.width = w
	
	def setDotSize(self, d):
		self.dotSize = d

	def draw(self, xpos, ypos, scale=1.0, orientation=0):
		terp = it.TurtleInterpreter()
		terp.place(xpos, ypos, orientation)
		terp.color(self.color)
		terp.setStyle(self.style)
		terp.setJitter(self.jitterSigma)
		terp.width(self.width)
		terp.drawString(self.string, self.distance*scale, self.angle)
	 
class Square(Shape):

	def __init__(self, distance=100, color=(0, 0, 0) ):
		''' Initializes Square object '''
		Shape.__init__(self, distance, 90, color, 'F-F-F-F-')
		
class Triangle(Shape):
	
	def __init__(self, distance=100, color=(0, 0, 0) ):
		''' Initializes Triangle object '''
		Shape.__init__(self, distance, 120, color, 'F-F-F-')
