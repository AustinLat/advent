class big_gen():
	
	def recitation(sequence):
		self.number_list = sequence
		while len(number_list) < 2020:
		#while True:
			if self.number_list[-1] not in self.number_list[:-1]:
			
				self.number_list.append(0)
						
			else:
				self.number_list.append(index_finder())
				#last_occurance = len(number_list) -1- number_list[-2::-1].index(number_list[-1])	
				#yield (len(number_list)-(last_occurance))
				#number_list.append(len(number_list)-(last_occurance))
			
		print(self.number_list)

	def index_finder(self):
		last_occurance = len(self.number_list) -1- self.number_list[-2::-1].index(self.number_list[-1])	
		return next(len(self.number_list)-(last_occurance))



if __name__=="__main__":
	big_gen.recitation([0,3,6])
