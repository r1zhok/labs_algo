from collections import deque
from queue import Queue


def min_distance(size: int, start: tuple, end: tuple, row: list, col: list):
    graph = {start: start}
    possible_pos = Queue()
    possible_pos.put(start)
    find_point = False
    count = 0

    while True:
        current_pos = possible_pos.get()
        count_of_nodes = []
        count += 1

        for i in range(0, 8):
            new_pos = (current_pos[0] + row[i], current_pos[1] + col[i])
            if (0 <= new_pos[0] < size) and (0 <= new_pos[1] < size):
                if new_pos == end:
                    find_point = True
                count_of_nodes.append(new_pos)
                possible_pos.put(new_pos)

        graph[current_pos] = count_of_nodes

        if find_point:
            print(count)
            return min_depth_bfs(graph, start, end)


def min_depth_bfs(graph, start, end) -> int:
    visited = set()
    queue = deque([(start, 1)])
    count = 0

    while queue:
        node, depth = queue.popleft()
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                count += 1
                if neighbor == end:
                    print(count)
                    return depth
                queue.append((neighbor, depth + 1))

    return -1


if __name__ == '__main__':
    file = open("input.txt", "r")

    size_of_desk = int(file.readline())
    start_point = eval(file.readline())
    end_point = eval(file.readline())

    file.close()

    row = [2, 2, -2, -2, 1, 1, -1, -1]
    col = [-1, 1, 1, -1, 2, -2, 2, -2]

    print(min_distance(size_of_desk, start_point, end_point, row, col))
