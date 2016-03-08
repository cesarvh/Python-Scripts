import operator

def letterSorter(names):
	"""
	>>> names = ["annie", "bonnie", "liz"]
	>>> letterSorter(names)
	["bonnie", "liz", "annie"]
	>>> names = ["abcdefg", "vi"]
	["abcdefg", "vi"]
	"""
	
	aVal = ord('a')
	letterVals = {}
	retVal = []
	for i in range(0, 26):
		letterVals[chr(aVal + i)] = i + 1
	namesDic = {}
	for name in names:
		nameTotal = 0
		for letter in name:
			nameTotal += letterVals[letter]
		namesDic[name] = nameTotal
	while len(namesDic) != 0:
		maxItem = min(namesDic.iteritems(), key=operator.itemgetter(1))[0]
		namesDic.pop(maxItem)
		retVal.append(maxItem)
	print retVal

