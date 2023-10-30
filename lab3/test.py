import unittest
from BinaryTree import BinaryTree
from lab3.lab3 import binary_tree_diameter


class MinLengthTest(unittest.TestCase):

    def test1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(3)
        root.right = BinaryTree(2)
        root.left.left = BinaryTree(7)
        root.left.right = BinaryTree(4)
        root.left.left.left = BinaryTree(8)
        root.left.right.right = BinaryTree(5)
        root.left.right.right = BinaryTree(6)
        root.left.left.left = BinaryTree(9)

        self.assertEqual(binary_tree_diameter(root), 6)


if __name__ == '__main__':
    unittest.main()
