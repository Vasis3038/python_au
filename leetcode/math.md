# math

+ [Reverse Integer](#reverse-integer)
+ [Palindrome Number](#palindrome-number)
+ [Fizz Buzz](#fizz-buzz)
+ [Base 7](#base-7)
+ [Fibonacci Number](#fibonacci-number)
+ [Sqrt(x)](#sqrt(x))
+ [Largest Perimeter Triangle](#largest-perimeter-triangle)
+ [K Closest Points to Origin](#k-closest-points-to-origin)

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

## Fizz Buzz


https://leetcode.com/problems/fizz-buzz/

```python
def fizzBuzz(self, n: int) -> List[str]:
    sch = 1
    lst = []       
    while sch <= n:
        if (sch % 3 == 0) and (sch % 5 == 0) :
            lst.append("FizzBuzz")
        else:
            if sch % 3 == 0:
                lst.append("Fizz")
            else:
                if sch % 5 == 0:
                    lst.append("Buzz")
                else:      
                    a = str(sch)
                    lst.append(a)
        sch = sch + 1   
    return lst
```

## Base 7


https://leetcode.com/problems/base-7/submissions/

```python
def convertToBase7(self, num: int) -> str:
    a = []
    t = num
    if num < 0:
        num *= -1
    if num == 0:
        return '0'
    while num > 0:
        b = str(num % 7)
        a.append(b)
        num = num // 7
    if t < 0:
        a.append('-')
    a.reverse()
    return "".join(a)
```

## Fibonacci Number


https://leetcode.com/problems/fibonacci-number/

```python
def fib(self, N: int) -> int:
    a = 0
    b = 1
    c = 0
    sch = 1
    if N == 0:
        return 0
    if N == 1:
        return 1
    while(sch < N):
        c = a + b
        a = b
        b = c
        sch += 1
    return c
```

## Sqrt(x)


https://leetcode.com/problems/sqrtx/

```python
def mySqrt(self, x: int) -> int:
    n = 0
    while (n+1) * (n+1) <= x:
            n = n + 1
    return n
```

## Largest Perimeter Triangle


https://leetcode.com/problems/largest-perimeter-triangle/

```python
def largestPerimeter(self, A: List[int]) -> int:
    A.sort(reverse = True)
    for i in range(len(A)-2):
        if A[i] < A[i+1] + A[i+2]:
            return A[i] + A[i+1] + A[i+2]
    return 0
```

## K Closest Points to Origin


https://leetcode.com/problems/k-closest-points-to-origin/

```python
def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    return sorted(points, key = lambda pair:(pair[0]**2+pair[1]**2))[:k]
```