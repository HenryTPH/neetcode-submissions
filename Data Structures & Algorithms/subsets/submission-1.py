class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start: int, path: List[int]):
            res.append(path.copy())

            for i in range(start, len(nums)):
                # Choose
                path.append(nums[i])

                # Explore
                backtrack(i + 1, path)

                # Backtrack
                path.pop()

        backtrack(0, [])

        return res