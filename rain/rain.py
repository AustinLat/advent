import operator



def navigation():    
    with open("input.txt", "r") as r:
         data = r.read()
         data = data.splitlines()

    print(data)
    direction = 90
    grid = (0, 0)
    for instruction in data:
        print(instruction)
        print(f'before movement - direction is {direction}')

        inst = instruction[0]
        distance = int(instruction[1:])
        if inst == "R":
            direction = direction + distance
            if direction > 360:
                direction = direction - 360
            if direction == 0:
                direction = 360
        if inst == "L":
            direction = direction - distance
            if direction < 0:
                direction = direction + 360
            if direction == 0:
                direction = 360

        if inst == "F":
            if direction == 90:
                grid = tuple(map(operator.add, grid, (0, distance)))  
            elif direction == 360:
                grid = tuple(map(operator.add, grid, (distance, 0)))
            elif direction == 180:
                grid = tuple(map(operator.add, grid, (-(distance), 0)))
            elif direction == 270:
                grid = tuple(map(operator.add, grid, (0, -(distance))))
        elif instruction[0] == "N":
            grid = tuple(map(operator.add, grid, (distance, 0)))
        elif instruction[0] == "E":
            grid = tuple(map(operator.add, grid, (0, distance)))
        elif instruction[0] == "S":
            grid = tuple(map(operator.add, grid, (-(distance), 0)))
        elif instruction[0] == "W":
            grid = tuple(map(operator.add, grid, (0, -(distance))))
      
        print(f'after movement direction is {direction}')        
        print(grid)
    manhattan = (abs(grid[0])) + (abs(grid[1]))
    return manhattan

print(navigation())

#if __name__ == "__main__":
#    navigation()
