def part1():
	left, right, total=[], [], 0
	for line in [list(map(int, line.split())) for line in open("01_input.txt", "r").readlines()]:
		left.append(line[0])
		right.append(line[1])
	for i in range(len(left)):
		total+=abs(min(left) - min(right))
		left.remove(min(left))
		right.remove(min(right))
	print(total)

def part2():
	lines=open("01_input.txt", "r").readlines()
	left, right, total, similarity=[], [], 0, 0
	for line in lines:
		line=list(map(int, line.split()))
		left.append(line[0])
		right.append(line[1])
	similarity=sum([num*len([amount for amount in right if amount==num]) for num in left])
	for i in range(len(left)):
		total+=abs(min(left) - min(right))
		left.remove(min(left))
		right.remove(min(right))
	print(total, similarity)

part1()