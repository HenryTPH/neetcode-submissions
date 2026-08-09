class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        charactes = {')': '(', '}': '{', ']': '['}
        for ch in s:
            if ch in {'(', '[', '{'}:
                stack.append(ch)
            else:
                if not stack:
                    return False
                curr = stack.pop()
                if curr != charactes[ch]:
                    return False
        return not stack