def printLine(filename, count):
	fl = open(filename, 'rb')
	count = 0

	for lines in fl:
		lines = lines.strip().split(',')
		count += 1
		print lines
	print count

printLine('sample.txt', 2)