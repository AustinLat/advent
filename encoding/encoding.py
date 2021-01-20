with open("input.txt", "r") as r:
    data = r.read()
    data = data.splitlines()

def odd_man_out(sum_to):

    for num in range(sum_to, len(data)):
        checker = False
        for i in range((num - sum_to), (num)):
            for n in range((num - sum_to), (num)):
                if data[i] == data[n]:
                    continue
                if int(data[i]) + int(data[n]) == int(data[num]):
                    checker = True
        if checker is False:
            return int(data[num])
# print(odd_man_out(25))

#First part
def in_a_row():
    odd_number = odd_man_out(25)
    for num in range(len(data)):
        total_tracker = [int(data[num])]
        for i in range(num+1, len(data)):
            total_tracker.append(int(data[i]))
            if sum(total_tracker) == odd_number:
                print(min(total_tracker) + max(total_tracker))

in_a_row()
