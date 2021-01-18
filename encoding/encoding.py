# with open("input.txt", "r") as r:
#     data = r.read()
#     data = data.splitlines()

data = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

data = data.splitlines()

def odd_man_out(sum_to):
    index = sum_to
    while index != len(data):
        for i in range((index - sum_to), (index)):
            print(data[i])
            for n in range((index - sum_to), (index)+1):

                # print(data[n])
                if data[i] == data[n]:
                    continue
                if data[i] + data[n] == data[index]:
                    print("got it")

        index += 1


odd_man_out(5)
