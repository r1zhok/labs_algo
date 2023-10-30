from BinaryTree import BinaryTree
from queue import Queue


def binary_tree_diameter(tree: BinaryTree) -> int:
    if tree is None:
        return 0

    leaf_diameters = []
    queue = Queue()
    count = 1

    while True:
        if (tree.left is not None) and (tree.right is not None):
            length_left = cross_for_binary_tree(tree.left)
            length_right = cross_for_binary_tree(tree.right)
            for i in range(0, len(length_left)):
                for j in range(0, len(length_right)):
                    leaf_diameters.append(length_left[i] + length_right[j])
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

    return max(leaf_diameters)


def cross_for_binary_tree(vertex: BinaryTree) -> list:
    count = 1
    next_counter = 1
    massive = []
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
        elif vertex.right is not None:
            count += 1
            vertex = vertex.right
        else:
            massive.append(count)
            if queue.empty():
                break
            else:
                vertex = queue.get()
                count = queue_length.get()

    return massive


if __name__ == '__main__':
    root = BinaryTree(1)
    root.left = BinaryTree(3)
    root.right = BinaryTree(2)
    root.left.left = BinaryTree(7)
    root.left.right = BinaryTree(4)
    root.left.left.left = BinaryTree(8)
    # root.left.right.right = BinaryTree(5)
    # root.left.right.right.right = BinaryTree(6)
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
