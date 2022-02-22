class Harmless:
	def __init__(self):
		''' Constructor for this class. '''
		# Create some member animals
		self.members = ['Sparrow', 'Robin', 'Duck', 'Goldfish', 'Zeprafish']
	def printMembers(self):
		print('Printing members of the Harmless class')
		for member in self.members:
			print('\t%s ' % member)
