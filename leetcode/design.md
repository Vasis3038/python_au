# design

+ [Min Stack](#min-stack)
+ [Implement Queue using Stacks](#implement-queue-using-stacks)

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