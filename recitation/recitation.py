def recitation(sequence):
	number_list = sequence
	while len(number_list) < 2020:
		if number_list[-1] not in number_list[:-1]:
			number_list.append(0)
		else:
			last_occurance = len(number_list) -1- number_list[-2::-1].index(number_list[-1])	
			number_list.append(len(number_list)-(last_occurance))
		print(number_list)
	print(number_list[-1])


if __name__=="__main__":
	recitation([10,16,6,0,1,17])
	
