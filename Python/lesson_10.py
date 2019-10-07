nameStr = raw_input('Enter names separate by ,:')
names = nameStr.split(',')

assignmentStr = raw_input('Enter assignments separate by ,:')
assignments = assignmentStr.split(',')

gradeStr = raw_input('Enter grades separate by ,:')
grades = gradeStr.split(',')

for i in xrange(0, len(names)):
	print ('''
Hi %s,

This is a reminder that you have %d assignments left to submit before you can graduate. Your current grade is %d and can increase to %d if you submit all assignments before the due date.

	''' % (names[i], int(assignments[i]), int(grades[i]), int(grades[i]) + 2 * int(assignments[i])))