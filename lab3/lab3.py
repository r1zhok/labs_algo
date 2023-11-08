from BinaryTree import BinaryTree
from queue import Queue


def binary_tree_diameter(tree: BinaryTree) -> int:
    if tree is None:
        return 0

    massive = []
    queue = Queue()
    count = 1

    while True:
        if (tree.left is not None) and (tree.right is not None):
            length_left = cross_for_binary_tree(tree.left, 9, False, massive)
            length_right = cross_for_binary_tree(tree.right, 5, False, massive)
            if length_right[1] and length_left[3]:
                return length_left[0] + length_right[2]
            else:
                massive.clear()
            if tree.left is not None:
                if count == 1:
                    queue.put(tree.right)
                tree = tree.left
            else:
                tree = tree.right
            count += 1
        elif tree.left is not None:
            tree = tree.left
        elif tree.right is not None:
            tree = tree.right
        else:
            if queue.empty():
                break
            else:
                tree = queue.get()


def cross_for_binary_tree(vertex: BinaryTree, point: int, check: bool, massive: list):
    count = 1
    next_counter = 1
    queue = Queue()
    queue_length = Queue()
    while True:
        if (vertex.left is not None) and (vertex.right is not None):
            if next_counter % 2 == 1:
                next_counter += 1
                queue.put(vertex)
                queue_length.put(count)
                vertex = vertex.left
                count += 1
            else:
                vertex = vertex.right
                next_counter += 1
                count += 1
        elif vertex.left is not None:
            count += 1
            vertex = vertex.left
            if vertex.value == point:
                check = True
                massive.append(count)
                massive.append(check)
                return massive
        elif vertex.right is not None:
            count += 1
            vertex = vertex.right
            if vertex.value == point:
                check = True
                massive.append(count)
                massive.append(check)
                return massive
        else:
            if queue.empty():
                if vertex.value == point:
                    check = True
                    massive.append(count)
                    massive.append(check)
                    return massive
                return [0, False]
            else:
                vertex = queue.get()
                count = queue_length.get()


if __name__ == '__main__':
    root = BinaryTree(1)
    root.left = BinaryTree(3)
    root.right = BinaryTree(2)
    root.left.left = BinaryTree(7)
    root.left.right = BinaryTree(4)
    root.left.left.left = BinaryTree(8)
    root.left.right.right = BinaryTree(5)
    #root.left.right.right.right = BinaryTree(6)
    root.left.left.left.left = BinaryTree(9)

    tree2 = BinaryTree(1)
    tree2.left = BinaryTree(2)
    tree2.right = BinaryTree(3)
    tree2.right.left = BinaryTree(4)
    tree2.right.right = BinaryTree(5)

    print(binary_tree_diameter(root))
    # print(binary_tree_diameter(tree2))
    # print(binary_tree_diameter(
    # BinaryTree(1, left=BinaryTree(2, left=BinaryTree(4)), right=BinaryTree(3, right=BinaryTree(5)))))
