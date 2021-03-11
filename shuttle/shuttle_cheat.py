from math import gcd


def lcm(a):
	lcm = a[0][0]
	for i in a[1:]:
		lcm = lcm * i[0] // gcd(lcm, i[0])
	return lcm

with open("input.txt") as file:
	data = file.read().split("\n")

buses = []
offset = 0
for x in data[1:][0].split(","):
	if x != "x":
		buses.append([int(x), offset])
	offset += 1

buses.sort()

value = 1
add_to = 1
for i in range(1, len(buses)):
	good = False
	while good == False:
		good = True
		for j in range(0, i+1):
			if (value + buses[j][1]) % buses[j][0] != 0:
				good = False
				break
		if good == True:
			add_to = lcm(buses[:j])
			break
		else:
			value += add_to
			
print("SOLUTION IS " + str(value))	
