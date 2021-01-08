def binary():
    with open("input.txt",'r') as fh:
        all_lines = fh.read()
    high_chair = 0

    seat_list = []
    for line in all_lines.splitlines():
    #Find the row number
        row = [0, 127]
        for letter in line[:7]:
            if letter == "F":
                row[1] = int((row[0]+row[1]+1)/2) - 1
            elif letter == "B":
                row[0] = int((row[0]+row[1]+1)/2)
        row = row[0]
    #Find the collum
        col = [0, 7]
        for letter in line[7:]:
            if letter == "L":
                col[1] = int((col[0]+col[1]+1)/2) - 1
            elif letter == "R":
                col[0] = int((col[0]+col[1]+1)/2)
        col = col[0]
        seat_id = ((row * 8) + col)

        seat_list.append(seat_id)

    #find largest seat ID
        # if seat_id > high_chair:
        #     high_chair = seat_id

    my_seat = []
    last_seat = 69
    for seat in sorted(seat_list):
        if seat != last_seat+1:
            my_seat.append(seat)
        last_seat = seat
    print(my_seat[0]-1)




binary()
