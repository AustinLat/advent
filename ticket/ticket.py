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
    error_rate = 0
    ticket_lines = chunks[2].splitlines()[1:]
    ##looping through tickets
    for line in ticket_lines:
    	##looping through ticket numbers
    	for number in line.split(","):
    	    ##checking neighbors ticket numbers against all rules
            valid = False
            for rul, rnge in valid_ranges.items():
                valid = number_validation(number, rnge)
                if valid == True:
                    break
            if valid == False:
                error_rate += int(number)
    print(error_rate)		 

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
    
				

if __name__=="__main__":
	ticket()
