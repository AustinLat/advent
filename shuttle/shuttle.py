def shuttle():
    with open("input.txt", "r") as r:
        data = r.read()
        data = data.splitlines()
    time = int(data[0])
    start_t = time
    buses = data[1].split(",")
    buses[:] = [int(i) for i in buses if i != "x"]
    
    
         
    for bus in buses:
        if time % bus == 0:
            wait_time = time - start_t
            print(wait_time * bus)
            break
        time += 1

if __name__ == "__main__":
    shuttle()
