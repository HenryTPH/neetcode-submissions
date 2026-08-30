class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Return: maximum amount of money you can rob
        dfs(i): The max amount of money can rob at house i
        """
        memo = {}

        def dfs(house):
            if house >= len(nums):
                return 0

            if house in memo:
                return memo[house]
            
            memo[house] = max(nums[house] + dfs(house + 2), 0 + dfs(house + 1))

            return memo[house]
        
        return dfs(0)
