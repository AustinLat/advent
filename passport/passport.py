def passport():
    #opening and reading input file
    f = open("input.txt", "r")
    contents = f.read()
    f.close()

    #Converting each passport into a dictionary
    passcount = 0
    scans = []
    for pas in contents.split("\n\n"):
        scans.append(pas.replace("\n", " "))
    for passp in scans:
        d = {}
        for i in passp.split():
            d[str(i.split(":")[0])] = str(i.split(":")[1])

    #Fintering passports
        if len(d) != 8 and len(d) != 7:
            continue
        if len(d) == 7 and "cid" in d:
            continue
        if int(d["byr"]) not in range(1920, 2003):
            continue
        if int(d["iyr"]) not in range(2010, 2021):
            continue
        if int(d["eyr"]) not in range(2020, 2031):
            continue
        try:
            d["hgt"] += 1
            continue
        except:
            if d["hgt"][-2:] != "in" and d["hgt"][-2:] != "cm":
                continue
            if d["hgt"][-2:] == "in" and int(d["hgt"][:-2]) not in range(59,77):
                continue
            if d["hgt"][-2:] == "cm" and int(d["hgt"][:-2]) not in range(150, 194):
                continue
        if d["ecl"] not in "amb blu brn gry grn hzl oth":
            continue
        if d["hcl"] == "z" or "#" not in d["hcl"]:
            continue
        if len(d["pid"]) != 9 and isinstance(d["pid"], int) == False:
            continue
        passcount += 1
    print(passcount)

passport()
