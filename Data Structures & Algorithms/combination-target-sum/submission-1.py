class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        rs = []

        def backtrack(start, path: List[int], target: int):
            if target == 0:
                rs.append(path.copy())
                return
            if target < 0:
                return
            
            for i in range(start, len(nums)):  
                path.append(nums[i])              
                backtrack(i, path, target - nums[i])
                path.pop()   

        backtrack(0, [], target)

        return rs