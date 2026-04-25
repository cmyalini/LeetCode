class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        taken = 0
        while queue:
            node = queue.popleft()
            taken += 1
            for n in graph[node]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    queue.append(n)
        return taken == numCourses