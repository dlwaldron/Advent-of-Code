def part1():
	total=0
	for mul in "".join(open("03_input.txt", "r").readlines()).split("mul("):
		if ")" in mul:
			mul=mul.split(",")
			if len(mul)!=1:
				total+=int([val if val.isnumeric() else 0 for val in mul][0])*int([val if val.isnumeric() and f"{val})" in mul[1] else 0 for val in mul[1].split(")")][0])
	print("{:^3,}".format(total))

def part2():
	total=0
	for instruction in "".join(open("03_input.txt", "r").readlines()).split("do()"):
		instruction=instruction.split("don't()")
		for mul in instruction[0].split("mul("):
			if ")" in mul:
				mul=mul.split(",")
				if len(mul)!=1:
					total+=int([val if val.isnumeric() else 0 for val in mul][0])*int([val if val.isnumeric() and f"{val})" in mul[1] else 0 for val in mul[1].split(")")][0])
	print("{:^3,}".format(total))

part1()
part2()
