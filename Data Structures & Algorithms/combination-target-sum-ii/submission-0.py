class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        rs = []

        def backtrack(pos: int, path: List[int], remain: int):
            if remain == 0:
                rs.append(path.copy())
                return

            for i in range(pos, len(candidates)):
                if candidates[i] > remain:
                    break

                if i > pos and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])
                backtrack(i + 1, path, remain - candidates[i])
                path.pop()

        backtrack(0, [], target)
        return rs