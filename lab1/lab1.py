def peak_length(array):
    massive = []
    result = 0
    trigger = False

    if len(array) < 3:
        return result
    for element in array:
        if not massive:
            massive.append(element)
        elif element < massive[-1]:
            massive.append(element)
            trigger = True
        elif element > max(massive) or trigger:
            if trigger:
                variable = massive_length(massive)
                if result < variable:
                    result = variable
            massive.append(element)
            trigger = False

    if trigger:
        variable = massive_length(massive)
        if result < variable:
            result = variable

    return result


def massive_length(massive):
    if len(massive) >= 3:
        if all(element <= massive[0] for element in massive):
            massive.clear()
            return 0
        result = len(massive)
        print(massive)
        massive.clear()
        return result
    else:
        massive.pop(0)
        return 0


print(peak_length([1, 3, 8, 9, 0, 1, 4, 8, 11, 12, 1, 2, 8, 9, 0]))
