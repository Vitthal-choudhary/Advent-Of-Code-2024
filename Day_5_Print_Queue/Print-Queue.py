import time
from collections import defaultdict


def sum_of_middle(valid_updates):
    sum = 0

    for update in valid_updates:
        sum += update[int(((len(update) - 1) / 2))]

    return sum


def part_1(dictionary, updates):
    valid_updates = []
    invalid_updates = []

    for i in range(len(updates)):
        results = []

        for j in range(len(updates[i]) - 1):
            current_value = updates[i][j]
            next_value_dictionary = dictionary[updates[i][j + 1]]

            if current_value in next_value_dictionary:
                results.append(False)
            else:
                results.append(True)

        if False not in results:
            valid_updates.append(updates[i])
        else:
            invalid_updates.append(updates[i])

    print("[+] Part One Solution")
    print(f">>> Sum of the results: {sum_of_middle(valid_updates)}")

    return invalid_updates


def part_2(dictionary, invalid_updates):
    valid_updates = invalid_updates.copy()

    for i in range(len(invalid_updates)):
        for _ in range(len(invalid_updates[i])):
            for j in range(len(invalid_updates[i]) - 1):
                current_value = invalid_updates[i][j]
                next_value_dictionary = dictionary[invalid_updates[i][j + 1]]

                if current_value in next_value_dictionary:
                    valid_updates[i][j] = invalid_updates[i][j + 1]
                    valid_updates[i][j + 1] = current_value

    print("[+] Part Two Solution")
    print(f">>> Sum of the results: {sum_of_middle(valid_updates)}")


def main():
    with open("input.txt") as file:
        content = file.read().splitlines()

        rules = [list(map(int, rule.split("|"))) for rule in content[0:1176]]
        updates = [list(map(int, update.split(","))) for update in content[1177:1367]]

        dictionary = defaultdict(list)

        for rule in rules:
            dictionary[rule[0]].append(rule[1])

        print()
        invalid_updates = part_1(dictionary, updates)
        print()
        part_2(dictionary, invalid_updates)


if __name__ == "__main__":
    print()

    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()

    print(f"\nTotal Time Taken: {end_time - start_time} seconds.")
