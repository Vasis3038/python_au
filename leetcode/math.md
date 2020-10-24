# math

+ [Reverse Integer](#reverse-integer)
+ [Palindrome Number](#palindrome-number)

## Reverse Integer


https://leetcode.com/problems/reverse-integer/

```python
def reverse(self, x: int) -> int:
    a = 0
    t = x
    if x < 0:
        x = x*(-1)
    while x > 0:
        a = a*10 + x%10
        x = x // 10
    if t < 0:
        a = a*(-1)
    if (a > 2147483647) or (a < -2147483648):
        return 0
    return a
```

## Palindrome Number


https://leetcode.com/problems/palindrome-number/

```python
def isPalindrome(self, x: int) -> bool:
    a = 0   
    t = x
    ret = 1
    if x < 0:
        return 0
    while x > 0:
        a = a*10 + x%10
        x = x // 10
    if t < 0:
        a = a*(-1)
    while t > 0:
        if t%10 != a%10:
            ret = 0          
        t = t // 10
        a = a // 10
    return ret
```

