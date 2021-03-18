from collections import Counter

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
		for number in line.split(","):
			##checking neighbors ticket numbers against all rules
			valid_ticket = False	
			for rul, rnge in valid_ranges.items():
				rngs = rnge.split(" or ")
				first_rng = rngs[0].split("-")
				second_rng = rngs[1].split("-")
				if int(number) in range(int(first_rng[0]), int(first_rng[1])+1) or int(number) in range(int(second_rng[0]), int(second_rng[1])+1):
					valid_ticket = True
			##adding valid tickets to new list
			if valid_ticket == False:
				valid_tickets.append(line)

	##working with valid ticket list to determine the correct rule order
	order = []
	for line in valid_tickets:
		for num_index, number in enumerate(line.split(",")):	
			for rul, rnge in valid_ranges.items():
				rngs = rnge.split(" or ")
				first_rng = rngs[0].split("-")
				second_rng = rngs[1].split("-")
				if int(number) in range(int(first_rng[0]), int(first_rng[1])+1) or int(number) in range(int(second_rng[0]), int(second_rng[1])+1):
					valid_ticket = True
					for i in valid_tickets: 	
						if int(i.split(",")[num_index]) not in range(int(first_rng[0]), int(first_rng[1])+1) and int(i.split(",")[num_index]) not in range(int(second_rng[0]), int(second_rng[1])+1):
							valid_ticket = False
					if valid_ticket == True:
						order.append((rul, num_index))	
	occurence_count = Counter(order)
	res=occurence_count.most_common(21)
	print(len(valid_tickets))
	print(res)
	#print(order)	
				

if __name__=="__main__":
	ticket()
