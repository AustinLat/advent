import numpy as np


def shuttle():
	with open("input.txt", "r") as r:
		data = r.read()
		data = data.splitlines()
	time = 0
	#buses = data[1].split(",")
	#buses[:] = [int(i) for i in buses if i != "x"]
	buses = np.array(data[1].split(","))

	while True:
	#for t in np.nditer(time):
		time = time + int(buses[0])
		if time % int(buses[0]) == 0:

			for index, bus in enumerate(np.nditer(buses)):

		#	for index, bus in enumerate(buses):
				temp_time = time + index
				if buses[index] == "x":
					continue	
				if temp_time % int(bus) == 0:
					if index == len(buses) - 1 and temp_time % int(buses[0]) == 0:
						return t
						
					continue
				break
		
		print(time)

if __name__ == "__main__":
    print(shuttle())
