def recitation(sequence):
	number_list = sequence
	while len(number_list) < 10:
		print(number_list)
		if number_list[-1] not in number_list[:-1]:
			number_list.append(0)
		else:
			last_occurance = len(number_list) - 1 - number_list[-2::-1].index(number_list[-1]) 
			number_list.append(len(number_list)-(last_occurance+1))
	print(number_list)

if __name__=="__main__":
	recitation([0,3,6])
	
