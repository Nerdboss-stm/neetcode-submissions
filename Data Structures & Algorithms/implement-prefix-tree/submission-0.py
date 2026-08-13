class PrefixTree:

    def __init__(self):
        self.root = {}
        

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.setdefault(ch,{})
        node["$"] = True
    
    def _walk(self, prefix: str):
        node = self.root
        for ch in prefix:
            if ch not in node:
                return None
            node = node[ch]
        return node


    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and "$" in node
        

    def startsWith(self, prefix: str) -> bool:
        node = self._walk(prefix)
        return node is not None
        
        