def ticket():
	with open("input.txt", "r") as f:
		data = f.read()
		chunks = data.split("\n\n")

	##making rule ditionary
	valid_ranges = {}
	for line in chunks[0].splitlines():
		rng = line.split(":")[1][1:]
		rule = line.split(":")[0]
		valid_ranges[rule] = rng


	ticket_lines = chunks[2].splitlines()[1:]
	valid_tickets = []
	##looping through tickets
	for line in ticket_lines:
		##looping through ticket numbers
			for number_index, number in enumerate(line.split(",")):
			##checking neighbors ticket numbers against all rules
			valid_ticket = True
	
			for rule_index, (rul, rnge) in enumerate(valid_ranges.items()):
				rngs = rnge.split(" or ")
				first_rng = rngs[0].split("-")
				second_rng = rngs[1].split("-")
				if int(number) in range(int(first_rng[0]), int(first_rng[1])+1) or int(number) in range(int(second_rng[0]), int(second_rng[1])+1):
					valid_ticket = True
			if valid_ticket == True:
				valid_tickets.append(line)
	print(len(ticket_lines))
	print(len(valid_tickets))	 
				

if __name__=="__main__":
	ticket()
