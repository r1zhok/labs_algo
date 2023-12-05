import unittest
from lab6.src.trie import push


class Test(unittest.TestCase):

    def test1(self):
        trie = push(["abandon", "abortion", "accident", "bring"])
        self.assertEqual(trie.search("abandon"), True)

    def test2(self):
        trie = push(["abandon", "abortion", "accident", "bring"])
        self.assertEqual(trie.find_pref("aba"), True)

    def test3(self):
        trie = push(["abandon", "abortion", "accident", "bring"])
        self.assertEqual(trie.find_pref("bring"), True)


if __name__ == '__main__':
    unittest.main()
