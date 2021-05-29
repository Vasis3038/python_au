# House Robber

+ [House Robber](#house-robber)

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