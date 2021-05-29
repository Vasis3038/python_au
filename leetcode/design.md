# design

+ [Min Stack](#min-stack)
+ [Implement Queue using Stacks](#implement-queue-using-stacks)
+ [Implement Stack using Queues](#implement-stack-using-queues)
+ [Design Twitter](#design-twitter)

## Min Stack

https://leetcode.com/problems/min-stack/

```python
def __init__(self):
    self.stack = []

def push(self, val: int) -> None:
    minval = self.getMin()
    if minval == None or val < minval:
        minval = val 
    self.stack.append((val,minval))

def pop(self) -> None:
    return self.stack.pop()

def top(self) -> int:
    return self.stack[-1][0]

def getMin(self) -> int:
    if not self.stack:
        return None
    else:
        return self.stack[-1][1]
```


## Implement Queue using Stacks

https://leetcode.com/problems/implement-queue-using-stacks/

```python
def __init__(self):
    self.queue = []
        
 def push(self, x: int) -> None:
    self.queue.append(x)

def pop(self) -> int:
    if len(self.queue) < 1:
        return None
    return self.queue.pop(0) 

def peek(self) -> int:
    if len(self.queue) < 1:
        return None
    return self.queue[0] 

def empty(self) -> bool:
    if len(self.queue) == 0:
        return True
    return False
```


## Implement Stack using Queues

https://leetcode.com/problems/implement-stack-using-queues/

```python
def __init__(self):
    self.container=deque()

def push(self, x: int) -> None:
    self.container.append(x)
        
def pop(self) -> int:
    return self.container.pop()   

def top(self) -> int:
    return self.container[-1]     

def empty(self) -> bool:
    return len(self.container)==0
```


## Design Twitter

https://leetcode.com/problems/design-twitter/

```python
def __init__(self):
    self.stack = list()
    self.fo = defaultdict(list)

def postTweet(self, userId: int, tweetId: int) -> None:
    self.stack.append([userId,tweetId]) 

def getNewsFeed(self, userId: int) -> List[int]:
    temp = list()
    for i in range(len(self.stack)-1,-1,-1):
        if self.stack[i][0] == userId or self.stack[i][0] in self.fo[userId]:
            temp.append(self.stack[i][1])
            if len(temp) == 10:
                break
    return temp 
        
def follow(self, followerId: int, followeeId: int) -> None:
    self.fo[followerId].append(followeeId)

def unfollow(self, followerId: int, followeeId: int) -> None:
    if followeeId in self.fo[followerId]:
        self.fo[followerId].remove(followeeId)
```