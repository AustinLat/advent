# with open("input.txt", "r") as data:
#     data = data.read().splitlines()
#     data = [line for line in data]

data = """nop +0
    acc +1
    jmp +4
    acc +3
    jmp -3
    acc -99
    acc +1
    jmp -4
    acc +6"""
data = data.splitlines()
data = [line for line in data]

visited = []
index = 0
aac = 0
command = data[index]
while True:
    visited.append(index)
    if index  == len(data):
        break

    if command.split(" ")[0] == "acc":
        aac += int(command.split(" ")[1])
        index = index + 1

    if command.split(" ")[0] == "jmp":
        if "+" in command.split(" ")[1]:
            number = int(command.split(" ")[1][1:])
        else:
            number = int(command.split(" ")[1])
        index = index + number

    if command.split(" ")[0] == "nop":
        index = index + 1



    if index in visited:
        index = visited[-2]

        if command.split(" ")[0] == "jmp":
            command = "nop" + " " + command.split(" ")[1]
        else:
            command = "jmp" + " " + command.split(" ")[1]

    command = data[index]



    print(visited)
    print(index)
    print(aac)
