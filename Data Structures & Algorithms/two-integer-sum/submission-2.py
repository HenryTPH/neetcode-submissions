class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result =[]
        my_table = dict()
        for i, num in enumerate(nums):
            if num not in my_table:
                my_table[num] = []
            my_table[num].append(i)
            
        for i, num in enumerate(nums):
            rs = target - num
            if rs not in my_table:
                continue
            else:
                if len(my_table[rs]) == 1 and my_table[rs][0] == i:
                    continue
                else:
                    for j in my_table[rs]:
                        if j == i:
                            continue
                        else:
                            return [i, j]
        return result