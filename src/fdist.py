#!/usr/bin/env python
'''
    fdist  Copyright (C) 2017  Aaron Thomas
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.

The hypothetical commands `show w' and `show c' should show the appropriate
parts of the General Public License.  Of course, your program's commands
might be different; for a GUI interface, you would use an "about box".

  You should also get your employer (if you work as a programmer) or school,
if any, to sign a "copyright disclaimer" for the program, if necessary.
For more information on this, and how to apply and follow the GNU GPL, see
<http://www.gnu.org/licenses/>.

  The GNU General Public License does not permit incorporating your program
into proprietary programs.  If your program is a subroutine library, you
may consider it more useful to permit linking proprietary applications with
the library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.  But first, please read
<http://www.gnu.org/philosophy/why-not-lgpl.html>.
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