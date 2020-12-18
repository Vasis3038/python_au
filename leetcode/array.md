# array

+ [Max Consecutive Ones](#max-consecutive-ones)
+ [Reshape the Matrix](#reshape-the-matrix)
+ [Flipping an Image](#flipping-an-image)
+ [Transpose Matrix](#transpose_matrix)
+ [Move Zeroes](#move-zeroes)
+ [Image Smoother](#image-smoother)
+ [Squares of a Sorted Array](#squares-of-a-sorted-array)

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

## Transpose Matrix


https://leetcode.com/problems/transpose-matrix/

```python
def transpose(self, A: List[List[int]]) -> List[List[int]]:
    B = []
    for i in range (len(A)):
        k = 0
        while k is not len(A[i]):
            if len(B) <= k:
                B.append([])
            B[k].append(A[i][k])
            k += 1
    return B
```

##  Move Zeroes


https://leetcode.com/problems/move-zeroes/

```python
def moveZeroes(self, nums: List[int]) -> None:
    j = 0
    for i in range(len(nums)):
        if nums[i] is not 0:
            nums[j] = nums[i]
            j += 1      
    for i in range(j, len(nums)):
        nums[i] = 0
```

## Image Smoother


https://leetcode.com/problems/image-smoother/

```python
def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
    lenm = len(M)
    lenn = len(M[0])
    M2 = copy.deepcopy(M)
    for i in range(lenm):
        M[i].append(-1)
    M.append([-1] * (lenn+1))
    for i in range(lenm):
        for j in range(lenn):
            sum1 = [M[i-1][j-1] , M[i][j-1] , M[i+1][j-1] , M[i-1][j] , M[i+1][j] , M[i-1][j+1] , M[i][j+1] , M[i+1][j+1]]
            sum2 = sum1.count(-1)
            M2[i][j] += sum(sum1) + sum2
            M2[i][j] = int(M2[i][j]//(9-sum2))
    return M2
```

## Squares of a Sorted Array


https://leetcode.com/problems/squares-of-a-sorted-array/

```python
def get_first_nonnegative(self, A: List[int]):
    for i, val in enumerate(A):
        if val >= 0:
            return i
    return -1
def sortedSquares(self, A: List[int]) -> List[int]:
    ind = self.get_first_nonnegative(A)
 
    if ind == -1:
        return [x ** 2 for x in A[::-1]]
    elif ind == 0:
        return [x ** 2 for x in A]
    else:
        left, right = ind -1, ind
        length = len(A)
        res = []
        while right < length and left >= 0: 
            if A[left] ** 2 < A[right] ** 2:
                res.append(A[left] ** 2)
                left -= 1
            else:
                res.append(A[right] ** 2)
                right += 1
        while left >= 0:
            res.append(A[left] ** 2)
            left -= 1  
        while right < length:
            res.append(A[right] ** 2)
            right += 1
        return res
```