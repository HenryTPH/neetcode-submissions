class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        # Build the graph and calculate the indegree
        for second, first in prerequisites:
            graph[first].append(second)
            indegree[second] += 1

        # Collect all courses that having indegree = 0 to the queue
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        processed_course = 0

        while queue:
            current_course = queue.popleft()
            processed_course += 1
            for next_course in graph[current_course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        if processed_course == numCourses:
            return True
        return False