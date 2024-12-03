def part1():
	left, right=[], []
	for line in [list(map(int, line.split())) for line in open("01_input.txt", "r").readlines()]:
		left.append(line[0])
		right.append(line[1])
	left.sort()
	right.sort()
	print("{:^3,}".format(sum([abs(left[val]-right[val]) for val in range(len(left))])))

def part2():
	left, right=[], []
	for line in [list(map(int, line.split())) for line in open("01_input.txt", "r").readlines()]:
		left.append(line[0])
		right.append(line[1])
	print("{:^3,}".format(sum([num*len([amount for amount in right if amount==num]) for num in left])))

part1()
part2()
