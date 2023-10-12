def min_length(n: int, c: int, free_sections: list) -> int:
    sorted_list = sorted(free_sections)
    print("----------start and sorted massive---------------")
    print(sorted_list)

    if (n < 2) or (c > n):
        return 0
    else:
        if c == 2:
            return sorted_list[len(sorted_list) - 1] - sorted_list[0]
        else:
            collector = result_func(sorted_list, c)
            print("---------my massive----------")
            print(collector)

    min_diff = collector[1] - collector[0]
    for i in range(2, len(collector)):
        min_diff = min(min_diff, collector[i] - collector[i - 1])

    print("--------result--------")
    return min_diff


def result_func(sorted_list, c):
    number = 100 / c
    variable = number
    max_number = sorted_list[-1]
    result = [sorted_list[0]]
    bonus = (sorted_list[0] / max_number) * 100

    for element in sorted_list:
        if number + bonus <= (element / max_number) * 100:
            result.append(element)
            number = number + variable

    return result


print(min_length(10, 5, [1, 2, 3, 4, 5, 10, 30, 40, 60, 90]))
