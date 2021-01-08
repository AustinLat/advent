def expenses():
    input_list = []
    f = open("../input.txt", "r")
    contents = f.read()
    for line in contents.splitlines():
        input_list.append(line)
    f.close()


    for num in input_list:
        for next_num in input_list:
            for third_num in input_list:
                if int(num) + int(next_num) + int(third_num) == 2020:
                    print(num, next_num, third_num)
                    print(int(num) * int(next_num) + int(third_num))

expenses()