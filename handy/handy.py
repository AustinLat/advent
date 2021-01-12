def handy():
    with open("input.txt", "r") as r:
        all_lines = r.read()
    #Split each rule, and find bags that can hold gold.
    bags_for_gold = []
    for rule in all_lines.splitlines():
        rule = rule.split("bags contain")
        if "shiny gold" in rule[1]:
            bags_for_gold.append(rule[0])
            bag_set = set(bags_for_gold)

    #Turn updated bag_set back to list for looping purposes.
    #loop through list, adding more bags that can eventually hold
    #gold, adding them to the set above to remove duplicates.

    while True:
        bags_for_gold = list(bag_set)
        for rule in all_lines.splitlines():
            rule = rule.split("bags contain")
            for bag in bags_for_gold:
                if bag in rule[1]:
                    bag_set.add(rule[0])

        #checking if bag_set constant equals the length of the
        #list used for looping.  If so, that means no new items were added
        #to the set, and while exits.

        if len(bag_set) == len(bags_for_gold):
            break

    print(len(bag_set))
handy()
