# string

+ [valid anagram](valid-anagram)
+ [reverse-string](reverse-string)

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

## Reverse String


https://leetcode.com/problems/reverse-string/

```python
def reverseString(self, s: List[str]) -> None:
    for i in range (len(s)):
        s.insert(i, s[len(s)-1])
        del s[len(s)-1]
    return s
```