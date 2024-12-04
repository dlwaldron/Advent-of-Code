def part1(total=0, lines=[line.strip() for line in open("04_input.txt", "r").readlines()]):
	for index, line in enumerate(lines):
		for pos, char in enumerate(line):
			if char!="X" or not 0<=pos<=len(line):
				continue
			for stats in [[-1, -1], [-1, 0], [-1, 1], [1, -1], [1, 0], [1, 1]]:
				newLine, newPos, word=index, pos, True
				for char in ["M", "A", "S"]:
					newLine+=stats[0]
					newPos+=stats[1]
					if (newLine<0 or newPos<0 or newLine>=len(lines) or newPos>=len(line)) or lines[newLine][newPos]!=char:
						word=False
						break
				if word:
					total+=1
		total+=line.count("XMAS")+line.count("SAMX")
	print("{:^3,}".format(total).strip())

def part2(total=0, lines=[line.strip() for line in open("04_input.txt", "r").readlines()]):
	for index, line in enumerate(lines):
		for pos, char in enumerate(line):
			if char!="A" or not (0<pos<len(line)-1 and 0<index<len(lines)-1):
				continue
			for i, j in [("M", "S"), ("S", "M")]:
				if ((lines[index+1][pos-1]==j and lines[index-1][pos+1]==i) or (lines[index+1][pos-1]==i and lines[index-1][pos+1]==j)) and ((lines[index+1][pos+1]==j and lines[index-1][pos-1]==i) or (lines[index+1][pos+1]==i and lines[index-1][pos-1]==j)):
					total+=1
					break
	print("{:^3,}".format(total).strip())

part1()
part2()
