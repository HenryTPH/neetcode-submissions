class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0 for _ in range(numCourses)]

        for second, first in prerequisites:
            graph[first].append(second)
            indegree[second] += 1

        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        order_list = []

        while queue:
            current_course = queue.popleft()
            order_list.append(current_course)
            for next_course in graph[current_course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        if len(order_list) == numCourses:
            return order_list
        
        return []