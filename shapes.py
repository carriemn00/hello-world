# shapes.py
# Carrie Nguyen
# CS151 F18
# VERSION 3

import turtle_interpreter as it
import random

class Shape:

	def __init__(self, distance = 100, angle = 90, color = (0, 0, 0), istring = '' ):
		''' Initializes Shape object '''
		self.distance = distance
		self.angle = angle
		self.color = color
		self.string = istring
 
	def setColor(self, c):
		self.color = c
		
	def setDistance(self, d):
		self.distance = d
		
	def setAngle(self, a):
		self.angle = a
		
	def setString(self, s):
		self.string = s

	def draw(self, xpos, ypos, scale=1.0, orientation=0):
		terp = it.TurtleInterpreter()
		terp.place(xpos, ypos, orientation)
		terp.color(self.color)
		terp.drawString(self.string, self.distance*scale, self.angle)
	 
class Square(Shape):

	def __init__(self, distance=100, color=(0, 0, 0) ):
		''' Initializes Square object '''
		Shape.__init__(self, distance, 90, color, '{F-F-F-F-}')
		
class Rectangle(Shape):
	
	def __init__(self, distance=100, color=(0,0,0) ):
		''' Initializes Rectangle object '''
		Shape.__init__(self, distance, 90, color, '{F-FF-F-FF-}')
		
class Triangle(Shape):
	
	def __init__(self, distance=100, color=(0, 0, 0) ):
		''' Initializes Triangle object '''
		Shape.__init__(self, distance, 60, color, '{-F--F--F-}')

class Trapezoid(Shape):
	
	def __init__(self, distance=100, color=(0, 0, 0) ):
		''' Initializes Trapezoid object '''
		Shape.__init__(self, distance, 60, color, '{-F-F-F-}')		
		
class Octagon(Shape):

	def __init__(self, distance=100, color=(0, 0, 0) ): 
		''' Initializes Octagon object '''
		Shape.__init__(self, distance, 45, color, 'F-F-F-F-F-F-F-F-')
		
class Cross(Shape):
	
	def __init__(self, distance=100, color=(0, 0, 0) ):
		''' Initializes Cross object '''
		Shape.__init__(self, distance, 90, color, '{F-F-F+F-F-F+F-F-F+F-F-F+}')

class Pentagon(Shape):
	
	def __init__(self, distance=100, color=(0, 0, 0) ): 
		''' Initializes Pentagon object '''
		Shape.__init__(self, distance, 72, color, 'F-F-F-F-F-')
		
class Star(Shape):
	
	def __init__(self, distance=100, color=(0, 0, 0) ):
		''' Initializes Star object '''
		Shape.__init__(self, distance, 72, color, '{F--F+F--F+F--F+F--F+F--F+}')

def main():
	""" test function that generates image that incorporates all shapes created in Shapes class"""
	
	sx = 500
	sy = 500
	terp = it.TurtleInterpreter(sx, sy)
	
	for i in range(5): 
		octagon = Octagon(distance = 50)
		octagon.draw(random.randint(-450,450),random.randint(300,400))

	for i in range(5): 
		cross = Cross(distance=25, color=(0,0.6,0.9))
		cross.draw(random.randint(-450,450),random.randint(200,300))
		
	for i in range(5): 
		pentagon = Pentagon(distance = 50)
		pentagon.draw(random.randint(-450,450),random.randint(-100,0))
		
	for i in range(5): 
		star = Star(distance=25, color=(0.5,0.7,0))
		star.draw(random.randint(-450,450),random.randint(-300,-200))
		
	terp.hold()

if __name__ == "__main__":
	main()