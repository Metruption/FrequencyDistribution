#!/usr/bin/env python
'''
 Frequency Distribution: A python module used to generated Frequency Distributions.
    Copyright (C) 2017  Aaron Thomas

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
'''
from statistics import mean
from math import ceil

class DataClass:
	'''
	Yeah, this is a bad name. But the stat professor just calls it a "class".
	'''
	def __init__(self, start, width):
		self.start = start - .5
		self.end = width + start + .5
		self.midpoint = mean([self.start, self.end])
		self.width = width
		self.members = []

	def size():
		return len(members)

	def add(self, data_point):
		'''
		@parms:
			data_point is a piece of the data
		if data_point is in this class adds it to this class and returns true
		otherwise returns false
		'''
		if data_point >= self.start and data_point < self.end:
			self.members.append(data_point)
			self.members.sort()
			return True
		else:
			return False

	def to_string(self):
		return "Bounds:\n    Start:{} End:{}\nSize: {}\n".format(self.start,self.end,len(self.members))



class FrequencyDistribution:
	def __init__(self, dataset, numclasses):
			self.dataset = dataset
			self.numclasses = numclasses
			self.dataset.sort()
			self.class_size = ceil((max(dataset)-min(dataset))/numclasses)
			self.classes = [DataClass(min(dataset) + i*self.class_size, self.class_size) for i in range(numclasses)]
			
			for data_point in self.dataset: #@todo(aaron): make this more efficent
				for class_ in self.classes:
					if class_.add(data_point):
						break