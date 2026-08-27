class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        List look like [[0, 1], [1, 2], [2, 4]]
        We can make ta graph like: first: second
        1 : 0 | 2 : 1 | 4 : 2
        Run from course 0 to course 4, at each course run DFS to check cycle.
        """
        graph = defaultdict(list)
        for second, first in prerequisites:
            graph[first].append(second)

        visited = set()
        visiting = set()

        def dfs(course: int) -> bool:
            if course in visiting:
                return True
            if course in visited:
                return False
            visiting.add(course)
            for node in graph[course]:
                if dfs(node):
                    return True
            visiting.remove(course)
            visited.add(course)
            return False

        for i in range(numCourses):
            if dfs(i):
                return False
        return True