with open("input.txt", "r") as data:
    data = data.read().splitlines()
    data = [line for line in data]

visited = []
index = 0
aac = 0

while True:

    if index + 1 == len(data):
        break
    visited.append(index)

    command = data[index]

    if index in visited:
        if command.split(" ")[0] == "jmp":
            command.split(" ")[0] = "nop"
            index = index + 1

        if command.split(" ")[0] == "nop":
            command.split(" ")[0] = "jmp"
            if "+" in command.split(" ")[1]:
                number = int(command.split(" ")[1][1:])
            else:
                number = int(command.split(" ")[1])
            index = index + number

    else:
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


# print(visited)
# for i in range(len(visited)):
    # print(data[i])
    # print(i)
print(aac)
