with open("input.txt", "r") as data:
    data = data.readlines()
    data = [line.strip() for line in data]


def get_acc():
    visited = []
    index = 0
    aac = 0
    while index not in visited:
        visited.append(index)

        command = data[index]
        command = command.split()
        cmd = command[0]
        cmd_value = int(command[1])

        if cmd == "acc":
            aac += cmd_value
            index = index + 1
        elif cmd == "jmp":
            index += cmd_value
        elif cmd == "nop":
            index += 1


    return aac

#part 2
def get_aac_end():
    visited = []
    index = 0
    aac = 0
    while index not in visited:
        visited.append(index)

        command = data[index]
        command = command.split()
        cmd = command[0]
        cmd_value = int(command[1])

        if cmd == "acc":
            aac += cmd_value
            index = index + 1
        elif cmd == "jmp":
            index += cmd_value
        elif cmd == "nop":
            index += 1

        if index == len(data):
            return aac, True
    return aac, False

for i in range(len(data)):
    if "jmp" in data[i]:
        data[i] = data[i].replace("jmp", "nop")
        acc, found = get_aac_end()
        if found:
            print(acc)
            break

    else:
        data[i] = data[i].replace("nop", "jmp")
