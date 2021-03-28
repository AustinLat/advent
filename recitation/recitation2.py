def recitation2(sequence):
    spoken = {}
    turn = 1
    for num, number in enumerate(sequence):
        spoken[number] = [num+1]
        turn += 1
        if turn == len(sequence):
            last = number
    first = True
    while turn != 30000001:
        if first:
            spoken[0].append(turn)
            first = False
            last = 0
        else:
            new_num = turn - 1 - spoken[last][-2]
            if new_num in spoken:
                first = False
                spoken[new_num].append(turn)
            else:
                first = True
                spoken[new_num] = [turn]
            last = new_num
        turn += 1
         
        #print(turn)
    print(last)

if __name__=="__main__":
    recitation2([10,16,6,0,1,17])        
