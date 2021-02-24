import numpy as np
def shuttle():
	with open("input.txt", "r") as r:
		data = r.read()
		data = data.splitlines()
	time = 0
	buses = data[1].split(",")
	#buses[:] = [int(i) for i in buses if i != "x"]
        np_buses = np.array(buses)            
    
	while True:
		time = time + int(buses[0])
		if time % int(buses[0]) == 0:

			for index, bus in enumerate(buses):
				time = time + index
				if buses[index] == "x":
					continue	
				if time % int(bus) == 0:
					if index == len(buses) - 1 and time % int(buses[0]) == 0:
						print(time)
					continue
				break
		
		print(time)

if __name__ == "__main__":
    shuttle()
