def handy():
    with open("input.txt", "r") as r:
        all_lines = r.read()
    # print(all_lines.splitlines())
    bags_for_gold = []
    for rule in all_lines.splitlines():
        rule = rule.split("bags contain")
        if "shiny gold" in rule[1]:
            bags_for_gold.append(rule[0])

    while True:
        bag_set = set(bags_for_gold)
        bags_for_gold = list(bag_set)
        for rule in all_lines.splitlines():
            rule = rule.split("bags contain")
            for bag in bags_for_gold:
                if bag in rule[1]:
                    bag_set.add(rule[0])

        if len(bag_set) == len(bags_for_gold):
            break

    print(len(bag_set))
handy()
