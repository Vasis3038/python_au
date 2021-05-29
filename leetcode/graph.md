# graph

+ [Course Schedule II](#course-schedule-II)
+ [Course Schedule](#course-schedule)
+ [Number of Islands](#number-of-islands)
+ [Is Graph Bipartite?](#is-graph-bipartite)
+ [Cheapest Flights Within K Stops](#cheapest-flights-within-k-stops)
+ [Cheapest Flights Within K Stops](#cheapest-flights-within-k-stops)
+ [Shortest Path in Binary Matrix](#shortest-path-in-binary-matrix)
+ [Maximum Depth of N-ary Tree](#maximum-depth-of-n-ary-Tree)

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


## Number of Islands

https://leetcode.com/problems/number-of-islands/

```python
def dfs(self, grid, row, col, n):
    if  0 <= row < len(grid) and 0 <= col < n and grid[row][col] == "1":
        grid[row][col] = "0"
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            self.dfs(grid, row + x , col + y, n)
        
def numIslands(self, grid: List[List[str]]) -> int:
    counter = 0
    m = len(grid)
    n = len(grid[0])
    for row in range(m):
        for col in range(n):
            if grid[row][col] == '1':
                self.dfs(grid, row, col, n)
                counter += 1
    return counter 
```


## Is Graph Bipartite?

https://leetcode.com/problems/is-graph-bipartite/

```python
def isBipartite(self, graph):
    blank = 0
    red = 1
    green = 2
    n = len(graph)
    visited = [blank]*n
    print(visited)
    for i in range(n):
        if not visited[i]:
            que = deque([i])
            visited[i] = red
            while que:
                i = que.popleft()
                for j in graph[i]:
                    if visited[i] == visited[j]:
                        return False
                    if not visited[j]:
                        visited[j] = 3 - visited[i]
                        que.append(j)
    return True
```


## Cheapest Flights Within K Stops

https://leetcode.com/problems/cheapest-flights-within-k-stops/

```python
def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    g = defaultdict(list)
    print(g)
    for f, t, p in flights:
        g[f].append((t, p))
    print(g)
    M = defaultdict(int)
    q = [(src, 0, 0)]
    r = float('inf')
    while q:
        t, w, p = q.pop(0)
        if p >= r or w > k+1:
            continue
        if t == dst:
            r = min(r, p)
        for n, np in g[t]:
            if M[n] == 0 or M[n] > p + np:
                M[n] = p + np
                q.append((n, w + 1, p + np))
    return r if r != float('inf') else -1
```


## Shortest Path in Binary Matrix

https://leetcode.com/problems/shortest-path-in-binary-matrix/

```python
def can_visit(self, i, j, grid, seen, n):
    if i >= 0 and i < n and j >= 0 and j < n and not grid[i][j] and (i,j) not in seen:
        return True
    return False
    

def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    seen = set()
    n = len(grid)
    if grid[0][0] or grid[n-1][n-1]:
        return -1
    q = deque()
    q.append((0, 0, 1))
    seen.add((0, 0))
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    while q:
        i, j, d = q.popleft()
        if i == n - 1 and j == n - 1:
            return d    
        for direc in directions:
            x = i + direc[0]
            y = j + direc[1]
            if self.can_visit(x, y, grid, seen, n):
                seen.add((x, y))
                q.append((x, y, d+1))
    return -1
```


## Maximum Depth of N-ary Tree

https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

```python
def maxDepth(self, root):
    d = 0
    if not root:
        return 0
    else:
        for n in root.children:
            print(n.val)
            d = max(self.maxDepth(n) , d)  
        return d + 1
```




