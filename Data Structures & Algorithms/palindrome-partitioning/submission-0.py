class Solution:
    def partition(self, s: str) -> List[List[str]]:
        rs = []

        def isPalindrome(s: str) -> bool:
            return s == s[::-1]

        def backtrack(start_pos: int, path: List[str]):
            if start_pos >= len(s):
                rs.append(path.copy())
                return
            
            for i in range(start_pos, len(s)):
                substring = s[start_pos: i + 1]

                if isPalindrome(substring):
                    path.append(substring)
                    backtrack(i + 1, path)
                    path.pop()

        backtrack(0, [])

        return rs