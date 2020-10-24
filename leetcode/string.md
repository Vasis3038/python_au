# string

+ [valid anagram](valid-anagram)

## Valid Anagram


https://leetcode.com/problems/valid-anagram/

```python
def isAnagram(self, s: str, t: str) -> bool:
    s = list(s)
    t = list(t)
    s.sort()
    t.sort()
    if len(s) != len(t):
        return 0
    n = len(t) - 1
    while(n != -1):
        if s[n] != t[n]:
            return 0
        n -= 1
    return 1
```