from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w in cur.children:
                cur = cur.children[w]
            else:
                cur.children[w] = TrieNode()
                cur = cur.children[w]
        cur.word = True

    def search(self, word: str) -> bool:
        return self.do_search(word, self.root, 0)


    def do_search(self, word: str, node: TrieNode, idx: int) -> bool:
        if idx == len(word):
            return node.word

        if word[idx] == '.':
            for ch in node.children:
                if self.do_search(word, node.children[ch], idx + 1):
                    return True
            return False
        else:
            if word[idx] not in node.children:
                return False
            else:
                return self.do_search(word, node.children[word[idx]], idx + 1)

