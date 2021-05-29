# dynamic-programming

+ [House Robber](#house-robber)
+ [House Robber II](#house-robber-II)

## House Robber

https://leetcode.com/problems/house-robber/

```python
def rob(self, nums: List[int]) -> int:
    profits = [0]
    for i in range(len(nums)):
        if i == 0:
            profits.append(nums[i])  
        else:
            p = max(profits[i], profits[i-1] + nums[i])
            profits.append(p) 
    return profits[-1]    
```


## House Robber II

https://leetcode.com/problems/house-robber-ii/

```python
def rob(self, nums: List[int]) -> int:
    if not nums: 
        return 0
    if len(nums)==1: return nums[0]
        
    def f(nums):
        prev_max = 0
        cur_max = 0
        for p in nums:
            temp = cur_max
            cur_max = max(cur_max, prev_max+p)
            prev_max = temp
        return cur_max  
    return max( f(nums[:-1]), f(nums[1:]))
```