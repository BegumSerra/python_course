class Dangerous:
	def __init__(self):
		''' Constructor for this class. '''
		# Create some member animals
		self.members = ['Tiger', 'Elephant', 'Wild Cat', 'Shark']
	def printMembers(self):
		print('Printing members of the Dangerous class')
		for member in self.members:
			print('\t%s ' % member)
class Fish:
        def __init__(self):
                ''' Constructor for this class. '''
                # Create some member animals
                self.members = ['Goldfish', 'Shark', 'Zeprafish']
        def printMembers(self):
                print('Printing members of the Fish class')
                for member in self.members:
                        print('\t%s ' % member)
