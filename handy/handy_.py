def handy():
    with open("input.txt", "r") as r:
        all_lines = r.read()

    bags_for_gold = []
    total_bags = 0
    for rule in all_lines.splitlines():
        rule = rule.split("bags contain")
        if "shiny gold" in rule[0]:

            bags = rule[1].split(",")
            for i in bags:
                bags_for_gold.append(i.strip().replace(".", "").rsplit(" ", 1)[0])


    for bag in bags_for_gold:
        total_bags += int(bag.split(" ", 1)[0])
    print(bags_for_gold)


    # while True:

    for rule in all_lines.splitlines():
        rule = rule.split("bags contain")
        rule_bags = rule[1].split(",")

        bag_index = 0
        for bag_in_list in bags_for_gold:

            if bag_in_list.split(" ", 1)[1].strip().replace(".", "") == rule[0].strip():

                total_bags += len(rule_bags) * int(bag_in_list.split(" ", 1)[0])
                for new_list_bag in rule_bags:
                    bags_for_gold.pop(bag_index)
                    if new_list_bag != " no other bags.":
                        bags_for_gold.insert(bag_index, new_list_bag.strip())

                bag_index += 1
    print(bags_for_gold)


handy()
