class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:

        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char] 
        current.is_end_word = True
        

    def search(self, word: str) -> bool:

        def dfs(node: TrieNode, index: int):

            # Caso base
            if index == len(word):
                return node.is_end_word

            char = word[index]

            # Caso del punto
            if char == ".":
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False

            # Caso de una letra normal
            if char not in node.children:
                return False

            return dfs(node.children[char], index + 1)

        return dfs(self.root, 0)


        
