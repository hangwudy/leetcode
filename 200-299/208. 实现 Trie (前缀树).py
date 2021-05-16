from collections import defaultdict


class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.isWord = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.root
        for w in word:
            current = current.children[w]
        current.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.root
        for w in word:
            current = current.children.get(w)
            if current is None:
                return False
        return current.isWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.root
        for p in prefix:
            current = current.children.get(p)
            if current is None:
                return False
        return True
