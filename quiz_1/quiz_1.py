def contains_exclamation(str):
	return '!' in str

def num_caps(str):
	count = 0
	for c in str:
		if c.isupper():
			count += 1
	return count

def is_excited(str):
	return (contains_exclamation(str) or num_caps(str) > 0.5 * len(str))

if __name__ == '__main__':
	print is_excited('hourhgeroeHGERUGHEROGHEROUHRE')