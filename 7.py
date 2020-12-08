import sys


def parse_description(desc):
    if "no other" in desc:
        return {}
    else:
        return {
            x.strip().split(" ", 1)[1].strip(): int(x.strip().split(" ", 1)[0].strip())
            for x in desc.split(",")
        }


def can_reach_gold(bag, bag_info):
    if bag_info[bag] == {}:
        return False
    if "shiny gold" in bag_info[bag].keys():
        return True
    return any([can_reach_gold(b, bag_info) for b in bag_info[bag]])


def count_bags(bag, bag_info):
    if bag_info[bag] == {}:
        return 1
    return (
        sum([(count_bags(b, bag_info) * count) for b, count in bag_info[bag].items()])
        + 1
    )


def main():
    bag_requirements = [x.strip(" \n.") for x in sys.stdin]
    bag_info = {}
    for br in bag_requirements:
        description_without_bag = br.replace("bags", "").replace("bag", "")
        bag_key, description = description_without_bag.split(" contain ")
        bag_key = bag_key.strip()
        if bag_key not in bag_info.keys():
            bag_info[bag_key] = {}

        bag_info[bag_key] = parse_description(description)

    ans1 = sum([can_reach_gold(bag, bag_info) for bag in bag_info.keys()])
    ans2 = count_bags("shiny gold", bag_info) - 1

    print(f"1: {ans1}")
    print(f"2: {ans2}")


main()
