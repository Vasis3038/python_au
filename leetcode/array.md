# array

+ [Max Consecutive Ones](max-consecutive-ones)
+ [Reshape the Matrix](reshape-the-matrix)
+ [Flipping an Image](flipping-an-image)

## Max Consecutive Ones


https://leetcode.com/problems/max-consecutive-ones/

```python
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    M = 0
    sch = 0
    for i in range (len(nums)):
        if nums[i] == 1:
            sch += 1
        if (i == len(nums)-1) or (nums[i+1] == 0):
            if sch > M:
                M = sch
            sch = 0  
```

## Reshape the Matrix


https://leetcode.com/problems/reshape-the-matrix/

```python
def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
    N = len(nums)
    n = len(nums[0])        
    if r*c != N*n :
        return nums

    lst = []
    for i in range(N):
        for j in range(n):
            lst.append(nums[i][j])
    k = 0
    newLst = [[0 for i in range(c)] for j in range(r)]
    for i in range(len(newLst)):
        for j in range(len(newLst[i])):
            newLst[i][j] = lst[k]
            k += 1
            
    return newLst 
```

## Flipping an Image


https://leetcode.com/problems/flipping-an-image/

```python
def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
    for i in range(len(A)):
        A[i].reverse()
        for j in range(len(A[i])):
            A[i][j] = 1 - A[i][j]
    return A
```