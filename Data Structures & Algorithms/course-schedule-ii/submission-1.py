class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for second, first in prerequisites:
            graph[first].append(second)

        state = {}
        order_list = []

        def dfs(course: int) -> bool:
            if state.get(course) == 1:
                return True
            if state.get(course) == 2:
                return False

            state[course] = 1
            for next_course in graph[course]:
                if dfs(next_course):
                    return True

            state[course] = 2
            order_list.append(course)
            return False

        for course in range(numCourses):
            if state.get(course, 0) == 0:
                if dfs(course):
                    return []
        order_list.reverse()
        return order_list