from collections import Counter


valid_tickets = []

with open("input.txt", "r") as f:
        data = f.read()
        chunks = data.split("\n\n")

def make_dic(chunk):
    valid_ranges = {} 
    for line in chunk[0].splitlines():
        rng = line.split(":")[1][1:]
        rule = line.split(":")[0]
        valid_ranges[rule] = rng 
    return valid_ranges

def ticket_maker(chunk): 
    return chunk[2].splitlines()[1:]

def ticket(tickets, dic):
    for line in tickets:
        ##looping through ticket numbers
        line_valid = True
        for number in line.split(","):
            ##checking neighbors ticket numbers against all rules
            valid = False
            for rul, rnge in dic.items():
                validation = number_validation(number, rnge)
                if validation == True:
                    valid = True
            if valid == False:
                line_valid = False
        if line_valid == True:
            valid_tickets.append(line)                    

##Helper function for running each number through all the tests
def number_validation(num, rng):
    rngs = rng.split(" or ")
    first_rng = rngs[0].split("-")
    second_rng = rngs[1].split("-")
    fst = (int(first_rng[0]), int(first_rng[1])+1)
    snd = (int(second_rng[0]), int(second_rng[1])+1)
    if int(num) in range(fst[0], fst[1])  or int(num) in range(snd[0], snd[1]):
        return True
    return False

def ticket_order(valid_ticket_list, dic):
	pair_list = []
	for ticket in valid_ticket_list:
		for index, number in enumerate(ticket.split(",")):
			for rul, rng in dic.items():
				if number_validation(number, rng):
					pair_list.append((index, rul))	
	print(len(valid_ticket_list))
	c = Counter(pair_list)
	print(c.most_common(21))

if __name__=="__main__": 
    ticket(ticket_maker(chunks), make_dic(chunks))
    ticket_order(valid_tickets, make_dic(chunks))
