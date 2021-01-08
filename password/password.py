def password():
    passwords = []
    f = open("input.txt", "r")
    contents = f.read()
    f.close()
    for line in contents.splitlines():
        passwords.append(line)
    print(passwords)
    validcount = 0

    for item in passwords:
        lettercount = 0
        count = item.split()[0]
        letter = item.split()[1][0]
        passwrd = item.split()[2]

        # for character in passwrd:
        #     if character == letter:
        #         lettercount += 1
        # if lettercount in range(int(count.split("-")[0]), int(count.split("-")[1])+1):
        #     validcount += 1

        if letter == passwrd[int(count.split("-")[0])-1]:
            lettercount += 1
        if letter == passwrd[int(count.split("-")[1])-1]:
            lettercount += 1
        if lettercount == 1:
            validcount += 1
    print(validcount)
password()