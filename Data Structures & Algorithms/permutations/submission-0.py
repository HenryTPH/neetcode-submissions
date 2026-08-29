class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        rs = []

        def backtrack(path: List[int]):
            if len(path) == len(nums):
                rs.append(path.copy())
                return

            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    backtrack(path)
                    path.pop()

        backtrack([])
        return rs