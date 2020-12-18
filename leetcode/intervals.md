+ [Non-overlapping Intervals](#non-overlapping-intervals)
+ [Merge Intervals](#merge-intervals)
+ [Insert Interval](#insert-interval)

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

## Merge Intervals


https://leetcode.com/problems/merge-intervals/

```python
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    i = 0
    while i < len(intervals) - 1:
        if intervals[i][1] >= intervals[i + 1][0]:
            if intervals[i][1] >= intervals[i + 1][1]:
                del intervals[i + 1]
            else:
                intervals[i][1] = intervals[i + 1][1]
                del intervals[i + 1]
            i -= 1
        i += 1
    return intervals 
```

## Insert Interval


https://leetcode.com/problems/insert-interval/

```python
def insert(self, intervals, newInterval):
    intervals.append(newInterval)
    intervals.sort()
    i = 0
    while i < len(intervals) - 1:
        if intervals[i][1] >= intervals[i + 1][0]:
            if intervals[i][1] >= intervals[i + 1][1]:
                del intervals[i + 1]
            else:
                intervals[i][1] = intervals[i + 1][1]
                del intervals[i + 1]
            i = i - 1
        i += 1
    return intervals
```