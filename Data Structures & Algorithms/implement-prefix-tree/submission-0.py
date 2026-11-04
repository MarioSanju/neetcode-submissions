class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()        

    def insert(self, word: str) -> None:
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_end_word = True

    def search(self, word: str) -> bool:

        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        if current_node.is_end_word == True:
            return True
        return False
        
    def startsWith(self, prefix: str) -> bool:

        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return True


        
        