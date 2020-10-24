# array

+ [max consecutive cnes](max-consecutive-ones)

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