def handy():
    with open("input.txt", "r") as r:
        all_lines = r.read()


    bag_count = 0
    bags_for_gold = {}
    for rule in all_lines.splitlines():
        rule = rule.split("bags contain")
        if "shiny gold" in rule[0]:
            bags = rule[1].strip().split(", ")
            for bag in bags:
                if bag[-1] == ".":
                    bag = bag[:-1]
                bag = bag.rsplit(' ', 1)[0]
                bag = bag.split(" ", 1)
                bags_for_gold[bag[1]] = int(bag[0])
                bag_count += int(bags_for_gold[bag[1]])

    while bags_for_gold:

        for rule in all_lines.splitlines():
            rule = rule.split("bags contain")
            new_bags = {}
            old_bags = {}
            for bag in bags_for_gold:
                if bag in rule[0]:
                    bags = rule[1].strip().split(", ")
                    for new_bag in bags:
                        if new_bag[-1] == ".":
                            new_bag = new_bag[:-1]
                        new_bag = new_bag.rsplit(' ', 1)[0]
                        new_bag = new_bag.split(" ", 1)
                        if new_bag[0] == "no":
                            old_bags[bag] = bags_for_gold[bag]
                            continue
                        else:
                            new_bags[new_bag[1]] = int(new_bag[0])
                            old_bags[bag] = bags_for_gold[bag]

            print(bag_count)
            bag_count += sum(new_bags.values()) * int(bags_for_gold[bag])
            for old in old_bags:
                del bags_for_gold[old]
            for new in new_bags:
                bags_for_gold[new] = new_bags[new]


    # print(bags_for_gold)
    # print(bag_count)

handy()
