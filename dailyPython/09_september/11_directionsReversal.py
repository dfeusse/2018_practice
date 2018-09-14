def solve(arr):
	# theres an array
	# keep the first two words of each item in the list
	# reverse the last two words
	# concat
	# split into two lists
	# reverse one list
	# aggregate each element in both lists
	begs = []
	ends = []
	for i in arr:
		begs.append(" ".join(i.split()[:2]))
		ends.append(" ".join(i.split()[2:]))
	#print begs, ends
	answer = []
	for a, b in zip(begs, reversed(ends)):
		answer.append(a + " " + b)
	return answer



print solve(['Begin on 3rd Blvd', 'Right on First Road', 'Left on 9th Dr'])#, ['Begin on 9th Dr', 'Right on First Road', 'Left on 3rd Blvd'])
print solve(["Begin on Road A","Right on Road B","Right on Road C","Left on Road D"])#,['Begin on Road D', 'Right on Road C', 'Left on Road B', 'Left on Road A'])
print solve(["Begin on Road A"])#,['Begin on Road A'])