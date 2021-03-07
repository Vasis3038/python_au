# string

+ [Valid Anagram](#valid-anagram)
+ [Reverse String](#reverse-string)
+ [Reverse Vowels of a String](#reverse-vowels-of-a-string)
+ [Reverse Words in a String III](#reverse-words-in-a-string-III)

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

## Reverse Vowels of a String


https://leetcode.com/problems/reverse-vowels-of-a-string/

```python
def reverseVowels(self, s: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
    s = list(s)
    lst = []
    for i, letter in enumerate(s):
        if letter in vowels:
            lst.append(s[i])
    sch = 1
    
    for i, letter in enumerate(s):
        if letter in vowels:
            s[i]=lst[len(lst) - sch]
            sch += 1
    s = ''.join(s)
    return s
```

## Reverse Words in a String III


https://leetcode.com/problems/reverse-words-in-a-string-iii/

```python
def reverseWords(self, s: str) -> str:
    s = s.split()
    for i in range(len(s)):
        s[i] = list(s[i])
        for j in range(len(s[i])):
            s[i].insert(j, s[i][len(s[i])-1])
            del s[i][len(s[i])-1]
        s[i] = ''.join(s[i])
    s = ' '.join(s)
    return s
```
