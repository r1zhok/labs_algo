class TrieNode:

    def __init__(self):
        self.next = {}
        self.endWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current_node = self.root

        for element in word:
            if element not in current_node.next:
                current_node.next[element] = TrieNode()
            current_node = current_node.next[element]

        current_node.endWord = True

    def search(self, word: str) -> bool:
        current_node = self.root

        for element in word:
            if element not in current_node.next:
                return False
            current_node = current_node.next[element]

        return current_node.endWord

    def find_pref(self, prefix) -> bool:
        current_node = self.root

        for element in prefix:
            if element not in current_node.next:
                return False
            current_node = current_node.next[element]

        return True


def push(pattern: list) -> Trie:
    trie = Trie()

    for element in pattern:
        trie.insert(element)

    return trie
