class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        table = {"2": "abc", 
        "3": "def", 
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
        }

        rs = []

        def backtrack(index: int, path: str):
            if index == len(digits):
                rs.append(path)
                return
            
            value = table[digits[index]]
            for c in value:
                backtrack(index + 1, path + c)

        backtrack(0, "")
        return rs