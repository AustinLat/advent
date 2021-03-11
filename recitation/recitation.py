def recitation(sequence):
    number_list = sequence
    count = 0
    while len(number_list) < 30000000:
        count+=1
        if number_list[-1] not in number_list[:-1]:		
            number_list.append(0)
        else:
            number_list.append(index_finder(number_list))	
            print(count)
    print(number_list[-1])

def index_finder(current_list):
    last_occurance = len(current_list) -1- current_list[-2::-1].index(current_list[-1])	
    return (len(current_list)-(last_occurance))


if __name__=="__main__":
    recitation([10,16,6,0,1,17])
