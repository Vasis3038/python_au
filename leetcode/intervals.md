+ [Non-overlapping Intervals](#non-overlapping-intervals)

## Non-overlapping Intervals


https://leetcode.com/problems/non-overlapping-intervals/

```python
def eraseOverlapIntervals(self, intervals):
    print(intervals)
    intervals.sort(key = lambda x:x[1])
    print(intervals)
    res = 0
    i, j = 0, 1
    while j < len(intervals):
        if intervals[i][1] > intervals[j][0]:
            res += 1 
            j += 1
        else:
            i = j
            j += 1
    return res     
```