import operator

with open("input.txt", "r") as r:
    data = r.read().strip()



neighbors = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

data = data.splitlines()

def coord_seats(seating):
    coords_seating = {}
    for row_count, row in enumerate(seating):
        for collum_count, seat in enumerate(row):
            coords_seating[(row_count, collum_count)] = seat
    return coords_seating

def occupied_seating(coord_seats):
    while True:
        new_seating = {}
        for coord, seat in coord_seats.items():
            occupied = 0
            for neighbor in neighbors:
                neighbor_coord = tuple(map(operator.add, coord, neighbor))

                if neighbor_coord not in coord_seats:
                    continue
                if coord_seats[neighbor_coord] == "#":
                    occupied += 1

            if seat == ".":
                new_seating[coord] = seat
            elif seat == "L":
                if occupied == 0:
                    new_seating[coord] = "#"
                else:
                    new_seating[coord] = seat
            elif seat == "#":
                if occupied >= 4:
                    new_seating[coord] = "L"
                else:
                    new_seating[coord] = seat

        if coord_seats == new_seating:
            return new_seating
        coord_seats = new_seating

def count_occupied():
    occupied_counter = 0
    for coord, seat in occupied_seating(coord_seats(data)).items():
        if seat == "#":
            occupied_counter += 1
    return occupied_counter

print(count_occupied())
