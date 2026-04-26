from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            courseMap[a].append(b)
        
        def dfs(course_number, visit_path):
            if len(courseMap[course_number]) == 0:
                return True
            visit_path.append(course_number)
            for pre_req in courseMap[course_number]:
                if pre_req in visit_path:
                    return False
                if not dfs(pre_req, visit_path):
                    return False
            visit_path.remove(course_number)
            courseMap[course_number] = []               
            return True
        
        for i in range(numCourses):
            if not dfs(i, []):
                return False
        return True

        