from queue import Queue


def find_way(graph: dict, broken_transitions: list, cities: list, gas_storages: list) -> None:
    queue = Queue()
    way_from_gas_storage_to_city = []
    visited = set()
    next_node = iter(graph)
    name_of_storage = ''
    node = 0
    is_storage_find = False
    count = 0

    while graph:
        if not node == list(graph.keys())[-1]:
            count += 1
            node = next(next_node)
            if node in gas_storages:
                queue.put(node)
                while queue.queue:
                    current_node = queue.get()
                    visited.add(current_node)

                    if way_from_gas_storage_to_city and current_node in gas_storages:
                        broken_transitions.append(
                            [name_of_storage, sorted(list(set(cities) - set(way_from_gas_storage_to_city)))])
                        way_from_gas_storage_to_city.clear()
                        name_of_storage = current_node
                    elif current_node in gas_storages:
                        name_of_storage = current_node
                        is_storage_find = True

                    graph_find(current_node, graph, visited, is_storage_find, way_from_gas_storage_to_city,
                               queue, count, broken_transitions, name_of_storage, cities)
        else:
            break


def graph_find(current_node, graph, visited, is_storage_find, way_from_gas_storage_to_city, queue, count,
               broken_transitions,
               name_of_storage, cities):
    if current_node in graph.keys():
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                if is_storage_find:
                    way_from_gas_storage_to_city.append(neighbor)
            queue.put(neighbor)
            count += 1
    elif not way_from_gas_storage_to_city:
        broken_transitions.append(
            [name_of_storage, sorted(list(set(cities) - set(way_from_gas_storage_to_city)))])
        way_from_gas_storage_to_city.clear()


def gas_for_penguins(cities: list, gas_storages: list, active_gas_storages: list) -> list:
    print(active_gas_storages[0])
    broken_transitions = []
    graph = {}
    unique_data = []
    seen_shelters = set()

    for active in active_gas_storages:
        gas_storage = active[0]
        city = active[1]

        if gas_storage not in graph:
            graph[gas_storage] = []

        graph[gas_storage].append(city)

    print(graph)

    find_way(graph, broken_transitions, cities, gas_storages)

    for item in broken_transitions:
        shelter_name = item[0]

        if shelter_name not in seen_shelters:
            unique_data.append(item)
            seen_shelters.add(shelter_name)

    return unique_data


def main(input_file, output_file):
    with open(input_file, 'r', encoding='UTF-8') as file:
        lines = file.readlines()

        cities = list(eval(lines[0].strip()))
        gas_storages = list(eval(lines[1].strip()))
        active_gas_storages = list(eval(lines[2].strip()))

        result = gas_for_penguins(cities, gas_storages, active_gas_storages)

    with open(output_file, 'w', encoding='UTF-8') as file:
        file.write(str(result))
