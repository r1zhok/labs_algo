from queue import Queue

file = open("input.txt", "r")

size_of_desk = file.readline()
start_point = file.readline()
end_point = file.readline()

file.close()

row = [2, 2, -2, -2, 1, 1, -1, -1]
col = [-1, 1, 1, -1, 2, -2, 2, -2]

size_of_desk = int(size_of_desk)
start_point = list(eval(start_point))
end_point = list(eval(end_point))


def min_distance(size: int, start: list, end: list) -> int:
    possible_pos = Queue()
    possible_length = Queue()
    possible_pos.put(start)
    possible_length.put(0)
    count = 0

    while possible_pos is not None:
        current_pos = possible_pos.get()
        current_length = possible_length.get()
        count += 1

        if current_pos == end:
            return current_length

        for i in range(0, 7):
            if (0 <= current_pos[0] + row[i] < size) and (0 <= current_pos[1] + col[i] < size):
                possible_pos.put([current_pos[0] + row[i], current_pos[1] + col[i]])
                possible_length.put(current_length + 1)

        print(count)


if __name__ == '__main__':
    print(min_distance(size_of_desk, start_point, end_point))
