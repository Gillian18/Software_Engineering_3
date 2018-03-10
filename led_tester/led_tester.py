# -*- coding: utf-8 -*-

"""Main module."""
import re
class LightTester(object):
	"""docstring for LightTester"""
	lights=None
	def __init__(self, N):
		self.size = N
		self.lights = [[False]* N for _ in range(N)]

	def apply(self,instructions):
		pat=re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
		for instructions in instructions:
			m=pat.match(instructions)
			if(m):
				cmd = m[1]
				x1 = int(m[2])
				y1 = int(m[3])
				x2 = int(m[4])
				y2 = int(m[5])
				if x1 > x2 :
					x1, x2 = x2, x1
				if y1 > y2:
					y1, y2 = y2, y1
				if x1 < 0:
					x1 = 0
				if y1 < 0:
					y1 = 0
				if x2 >= self.size:
					x2 = self.size-1
				if y2 >= self.size:
					y2 = self.size-1
				if x2 < 0:
					continue
				if y2 < 0:
					continue
				if x1 >= self.size:
					continue
				if y1 >= self.size:
					continue
				if cmd == 'turn on':
		  			for i in range(x1, x2+1):
		  				for j in range(y1, y2+1):
		  					self.lights[i][j] = True
				elif cmd == "turn off":
		  			for i in range(x1, x2+1):
		  				for j in range(y1, y2+1):
		  					self.lights[i][j] = False
				elif cmd == "switch":
					for i in range(x1, x2+1):
		  				for j in range(y1, y2+1):
		  					if self.lights[i][j] == True:
		  						self.lights[i][j] = False
		  					else:
		  						self.lights[i][j] = True

	def count(self):
		count = 0
		for i in range(self.size):
		  	for j in range(self.size):
		  		if self.lights[i][j] == True:
		  			count += 1
		return count
		
        
