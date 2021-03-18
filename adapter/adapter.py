with open("input.txt", "r") as r:
    data = r.read().splitlines()

def adapter_tester():
    with open("input.txt", "r") as r:
        data = r.read().splitlines()
    data = sorted(map(lambda x: int(x), data))
    single, triple = 0, 0
    last_number = 0

    for number in data:
        if number - last_number == 1:
            single += 1
        if number - last_number == 3:
            triple += 1
        last_number = number
    return single * (triple+1)


print(adapter_tester())

#part 2
def total_configurations():
    with open("input.txt", "r") as r:
        data = r.read().splitlines()


    data = sorted(map(lambda x: int(x), data))
    data.append(max(data)+3)
    single, double, triple = 0, 0, 0
    sol = {0:1}

    for number in data:
        sol[number] = 0
        if number - 1 in sol:
            sol[number]+=sol[number-1]
        if number - 2 in sol:
            sol[number]+=sol[number-2]
        if number - 3 in sol:
            sol[number]+=sol[number-3]
    print(sol)
    return sol[max(data)]

print(total_configurations())

