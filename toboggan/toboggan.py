def multi(x):
    return x * 35

def toboggan():
    r = open("input.txt", "r")
    contents = r.read()
    r.close()
    tree_list = []
    for line in contents.splitlines():
        tree_list.append(line*100)
    tree_count = 0
    horizontal = 0
    vert_count = 0
    for vertical in tree_list:

        if vert_count % 2 == 0:
            if vertical[horizontal] == "#":
                tree_count += 1
            horizontal += 1
        vert_count += 1
    print(tree_count)

toboggan()
# 80, 162, 77, 83, 37
