def docking():
    data = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""
    
    data = data.splitlines()
    for line in data:
        print(line)


if __name__ == "__main__":
    docking()
