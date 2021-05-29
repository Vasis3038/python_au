# graph

+ [Course Schedule II](#course-schedule-II)
+ [Course Schedule](#course-schedule)

## Course Schedule II

https://leetcode.com/problems/course-schedule-ii/

```python
from collections import deque
def dfs(self, curr, visited, adj_list, answer):
    visited[curr] = 1 
    for neighbor in adj_list[curr]:
        if neighbor not in visited:
            if self.dfs(neighbor, visited, adj_list, answer):
                return True
        elif visited[neighbor] == 1:
            return True
    visited[curr] = 2
    answer.appendleft(curr)
    return False
    

def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    adj_list = [[] for i in range(numCourses)]
    for course, pre in prerequisites:
        adj_list[pre].append(course)
    visited = {}
    answer = deque()
    for curr in range(numCourses):
        if curr not in visited:
            if self.dfs(curr, visited, adj_list, answer):
                return []
    return answer
```


## Course Schedule

https://leetcode.com/problems/course-schedule/

```python
from collections import deque
def dfs(self, curr, visited, adj_list, answer):
    visited[curr] = 1 
    for neighbor in adj_list[curr]:
        if neighbor not in visited:
            if self.dfs(neighbor, visited, adj_list, answer):
                return True
        elif visited[neighbor] == 1:
            return True
    visited[curr] = 2
    answer.appendleft(curr)
    return False
    

def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    adj_list = [[] for i in range(numCourses)]
    for course, pre in prerequisites:
        adj_list[pre].append(course)
    visited = {}
    answer = deque()
    for curr in range(numCourses):
        if curr not in visited:
            if self.dfs(curr, visited, adj_list, answer):
                return []
    if answer == []:
        return 0
    else:
        return 1
```