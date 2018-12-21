# turtle_interpreter.py
# VERSION 4
# Carrie Nguyen
# CS151 F18

import turtle
import random
import sys

class TurtleInterpreter:
	initialized = False
	
	def __init__(self, dx = 800, dy = 800):
		''' Initializes TurtleInterpreter object '''
		self.style = 'normal'
		self.jitterSigma = 2
		self.dotSize = 2
		if TurtleInterpreter.initialized:
			return
		TurtleInterpreter.initialized = True
		
		turtle.setup( dx, dy)
		turtle.tracer(False)
		
	def drawString( self, dstring, distance, angle = 0, color = None):
		""" Interpret the characters in string dstring as a series
		of turtle commands. Distance specifies the distance
		to travel for each forward command. Angle specifies the
		angle (in degrees) for each right or left command. The list of 
		turtle supported turtle commands is:
		F : forward
		- : turn right
		+ : turn left
		[ : save position and heading
		] : restore position and heading
		L : draws leaf
		R : draws rectangle
		Z : draws circle
		< : save color
		> : unsave color
		g : green
		y : yellow
		r : red
		b : blue
		{ : begin fill
		} : end fill
		"""
		
		modstring = ''
		modval = None
		modgrab = False
		stack = []
		colorstack = [] 
			
		for c in dstring:
		
			if c == '(':
				modstring = ''
				modgrab = True
				continue
			elif c == ')':
				modval = float(modstring)
				modgrab = False
				continue
			elif modgrab:
				modstring += c
				continue
		
			if c == 'F': 
				if modval == None:
					self.forward(distance)
				else:
					self.forward(distance * modval)
			if c == 'f': 
				if modval == None:
					self.forward(distance)
				else:
					self.forward(distance * modval)
			elif c == '-':
				if modval == None:
					turtle.right(angle)
				else:
					turtle.right(modval)
			elif c == '+':
				if modval == None:
					turtle.left(angle)
				else:
					turtle.left(modval)
			elif c == '!':
				if modval == None:
					w = turtle.width()
					if w > 1:
						turtle.width(w-1)
				else:
					turtle.width(modval)
			elif c == '[':
				stack.append(turtle.position())
				stack.append(turtle.heading())
			elif c == ']':
				turtle.up()
				turtle.setheading(stack.pop())
				x, y = stack.pop()
				self.goto(x, y)
				turtle.down()
			elif c == 'L': # semicircle leaf
				turtle.begin_fill()
				turtle.circle(distance,180) 
				turtle.end_fill()
			elif c == 'R': # rectangular vase
				turtle.color( random.random(), random.random(), random.random() )
				turtle.begin_fill()
				for i in range(4):
					turtle.forward(distance)
					turtle.right(angle)
				turtle.end_fill()
			elif c == 'Z': # berry
				turtle.begin_fill()
				turtle.circle(distance)
				turtle.end_fill()
			elif c == '<':
				colorstack.append(turtle.color()[0] )
			elif c == '>':
				turtle.color(colorstack.pop())
			elif c == 'g':
				turtle.color(0.15, 0.5, 0.2)
			elif c == 'y':
				turtle.color(0.8, 0.8, 0.3)
			elif c == 'r':
				turtle.color(0.7, 0.2, 0.3)
			elif c == 'b':
				turtle.color(0.3, 0.3, 0.8)
			elif c == '{': 
				turtle.begin_fill()
			elif c == '}':
				turtle.end_fill()
			
			modval = None
			turtle.update()

	def hold(self):
		'''Holds the screen open until user clicks or presses 'q' key'''

		# Hide the turtle cursor and update the screen
		turtle.hideturtle()
		turtle.update()
	
		# Close the window when users presses the 'q' key
		turtle.onkey(turtle.bye, 'q')
	
		# Listen for the q button press event
		turtle.listen()
	
		# Have the turtle listen for a click
		turtle.exitonclick()	
		
	def place(self, xpos, ypos, angle = None): 
		''' places turtle in the specified coordinate position and angle (if applicable)'''
		turtle.penup()
		turtle.goto(xpos, ypos)
		if angle != None:
			turtle.setheading(angle)
		turtle.pendown()
	
	def goto(self, xpos, ypos):
		turtle.penup()
		turtle.goto(xpos, ypos)
		turtle.pendown()	
	
	def orient(self, angle):
		turtle.setheading(angle)
		
	def color(self, c): 
		turtle.color(c)
		
	def width(self, w): 
		turtle.width(w)
		
	def setStyle(self, s):
		self.style = s
		
	def setJitter(self, j):
		self.jitterSigma = j
		
	def setDotSize(self, d):
		self.dotSize = d
		
	def forward(self, distance):
		if self.style is 'normal':
			turtle.forward(distance)
		elif self.style is 'jitter':
			x0, y0 = turtle.position()
			turtle.up()
			turtle.forward(distance)
			xf, yf = turtle.position()
			curwidth = turtle.width()
			
			jx = random.gauss(0, self.jitterSigma)
			jy = random.gauss(0, self.jitterSigma)
			kx = random.gauss(0, self.jitterSigma)
			ky = random.gauss(0, self.jitterSigma)
			
			turtle.width(curwidth + random.randint(0,2))
			turtle.goto((x0 + jx), (y0 + jy))
			turtle.down()
			turtle.goto((xf + kx), (yf + ky))
			turtle.up()
			turtle.goto(xf, yf)
			turtle.width(curwidth)
			turtle.down()
		elif self.style is 'jitter3':
			x0, y0 = turtle.position()
			turtle.up()
			turtle.forward(distance)
			xf, yf = turtle.position()
			curwidth = turtle.width()
			
			for i in range(3):
				jx = random.gauss(0,self.jitterSigma)
				jy = random.gauss(0,self.jitterSigma)
				kx = random.gauss(0, self.jitterSigma)
				ky = random.gauss(0, self.jitterSigma)
				turtle.width(curwidth + random.randint(0,2))
				turtle.goto(x0+jx, y0+jy)
				turtle.down()
				turtle.goto((xf + kx), (yf + ky))
				turtle.up()
				turtle.goto(xf, yf)
				turtle.width(curwidth)
				turtle.down()
		elif self.style is 'dotted':
			x0, y0 = turtle.position()
			turtle.up()
			turtle.forward(distance)
			xf, yf = turtle.position()
			curwidth = turtle.width()
			
			dx = xf - x0
			dy = yf - y0
			
			for 
			turtle.down()
			turtle.circle(self.dotSize)
			turtle.up()
			turtle.goto(xf, yf)
			turtle.width(curwidth)
			turtle.down()
			
		
