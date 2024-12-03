def isSafe(pLine, direction="decrease"):
	if pLine[0]-pLine[1]>0:
		direction="increase"
	for index in range(len(pLine)-1):
		difference=pLine[index]-pLine[index+1]
		if (difference<0 and direction=="increase") or (difference>0 and direction=="decrease") or not (-3<=difference<=3 and difference!=0):
			return
	return True

def part1():
	print(len([True for line in open("02_input.txt", "r").readlines() if isSafe(list(map(int, line.split())))]))

def part2():
	safe=0
	for line in open("02_input.txt", "r").readlines():
		line=list(map(int, line.split()))
		for i in range(-1, len(line)):
			if isSafe([val for index, val in enumerate(line) if index!=i])==True:
				safe+=1
				break
	print(safe)

part1()
part2()
