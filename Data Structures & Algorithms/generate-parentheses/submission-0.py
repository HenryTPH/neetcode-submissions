class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        rs = []

        def backtrack(o: int, c: int, path: str):
            if o == n and c == n:
                rs.append(path)
                return

            if o < n:
                backtrack(o + 1, c, path + "(")
            if c < o:
                backtrack(o, c + 1, path + ")")
        
        backtrack(0, 0, "")
        return rs