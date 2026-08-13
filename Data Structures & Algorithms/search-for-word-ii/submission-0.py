class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = {}
        # Reading words into trie
        for w in words:
            node = root
            for ch in w:
                node = node.setdefault(ch, {})
            node["$"] = w
        
        rows, cols = len(board), len(board[0])
        found = []
        def dfs (row, col, node):
            ch = board[row][col]
            if ch not in node:
                return
            next = node[ch]

            word = next.pop("$", None)

            if word:
                found.append(word)
            
            board[row][col] = "#"

            for dr, dc in ((1,0), (0,1), (-1,0), (0,-1)):
                nr, nc = row+dr, col+dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, next)
            
            board[row][col] = ch

            if not next:
                node.pop(ch)
            
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        
        return found


            




        