class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        rs = []

        def dfs(i: int, current: List[int]):
            if i >= n: 
                rs.append(current.copy())
                return
            
            # Choice A: Exclude nums[i]
            dfs(i + 1, current)

            # Choice B: Include nums[i]
            current.append(nums[i])
            dfs(i + 1, current)

            # Pop the nums[i] from the current for the next call
            current.pop()
        
        dfs(0, [])
        return rs