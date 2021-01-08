def customs():
    with open("input.txt", "r") as r:
        all_lines = r.read()
    number = 0
    for i in all_lines.split("\n\n"):
        # i = set(i.replace("\n", ""))
        # number += len(i)
        i = i.splitlines()
        number += len(set(i[0]).intersection(*i))

    print(number)


        # print(i)

customs()
