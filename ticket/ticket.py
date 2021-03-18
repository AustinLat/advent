def ticket():
<<<<<<< HEAD
    



if __name__=="__main__":
    ticket()
=======
	with open("input.txt", "r") as f:
		data = f.read()
		chunks = data.split("\n\n")
	valid_ranges = {}
	for line in chunks[0].splitlines():
		rng = line.split(":")[1][1:]
		rule = line.split(":")[0]
		valid_ranges[rule] = rng
	error_rate = 0
	ticket_lines = chunks[2].splitlines()[1:]
	for line in ticket_lines:
		for number in line.split(","):	
			valid = False
			for rul, rnge in valid_ranges.items():
				rngs = rnge.split(" or ")
				first_rng = rngs[0].split("-")
				second_rng = rngs[1].split("-")
				if int(number) in range(int(first_rng[0]), int(first_rng[1])+1) or int(number) in range(int(second_rng[0]), int(second_rng[1])+1):
					valid = True
			if valid == False:
				error_rate += int(number)
	print(error_rate)		 
				

if __name__=="__main__":
	ticket()
>>>>>>> 941ed98b191d821e0219023ccae4157c6ea83e0e
