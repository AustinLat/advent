def handy():
    with open("input.txt", "r") as r:
        all_lines = r.read()
    print(all_lines.splitlines())

handy()
