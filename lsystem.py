# lsystem.py
# VERSION 3
# Carrie Nguyen
# CS151F18

import sys
import random

class Lsystem: 

	def __init__(self, filename = None):
		''' initialize lsystem with base and rules
			optional filename '''
		self.base = '' 
		self.rules = {}
		
		if filename != None: 
			self.read(filename)
			
	def setBase (self, newbase):
		''' set base '''
		self.base = newbase
		
	def getBase(self):
		''' returns base '''
		return self.base
		
	def getRule(self, index):
		''' returns specified single rule from the rules field of self	'''
		return self.rules[index]
		
	def addRule(self, newRule):
		''' adds newRule to rules field of self '''
		self.rules[newRule[0]] = newRule[1:]
		
	def numRules(self):
		''' returns number of rules in rules list '''
		return len(self.rules)
		
	def read(self, filename):
		''' opens file, reads in lsystem info, resets base and rule fields, and stores info
		into appropriate fields '''
		
		fp = open(filename, "r" )
		
		for line in fp:
			words = line.split()
			if words[0] == "base":
				self.setBase(words[1])
			elif words[0] == "rule":
				self.addRule(words[1:])
		# print(words) TEST
		fp.close()
		
	def replace(self, istring):
		''' scan through string, test each character to see if there is rule
			if rule exists, then add replacement to new string
			if no rule exists, add character to new string 
		''' 
		tstring = ''
		for c in istring: 
			if c in self.rules:
				tstring += random.choice(self.rules[c])
			else:
				tstring += c 
		#print(tstring) #TEST
		return tstring
	
		
	def buildString(self, iterations):
		''' builds the lsystem string 
		'''
		nstring = self.base
		for i in range(iterations):
			nstring = self.replace(nstring)
		
		#print(nstring) #TEST
		return nstring
		
def main(argv):
	if len(argv) < 2:
		print('Usage: lsystem.py <filename>')
		exit()
	filename = argv[1]
	iterations = 2

	lsys = Lsystem()

	lsys.read( filename )

	print( lsys )
	print( lsys.getBase() )
	for i in range( lsys.numRules() ):
		rule = lsys.getRule(i)
		print( rule[0] + ' -> ' + rule[1] )

	lstr = lsys.buildString( iterations )
	print( lstr )
	
	return

if __name__ == "__main__":
	main(sys.argv)
					
		
						
		
