#Sara Gottlieb
#creating a new class that will use the grading system
#hard code the grade i.e a= 100, etc.
#then add or subtract depending on plus or minus

#overwrite the compare method in python to compare on the numeric_value
#that I assign
class Grade(object):

	def __init__(self, letter):
		self.letter = str(letter).upper()
		grading_dict_letter = { 'A': 95, 'B':85, 'C':75, 'D':65 , 'F': 55}
		self.numeric_value = grading_dict_letter[self.letter[0]] 
		if len(self.letter)>1:
			if self.letter[-1]=='-':
				self.numeric_value -= 3
			else:
				self.numeric_value += 3


	def __cmp__(self, other):
		return (self.numeric_value).__cmp__(other.numeric_value)


a = Grade('C-')
b = Grade('B+')
print a>b
print b>a