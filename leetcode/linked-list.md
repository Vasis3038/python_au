# linked-list

+ [Reverse Linked List](#reverse-linked-list)
+ [Middle of the Linked List](#middle-of-the-Linked-List)
+ [Palindrome Linked List](#palindrome-linked-list)
## Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/

```python
def reverseList(self, head: ListNode) -> ListNode:
    cur = head
    Next = None
    prev = None
    while cur != None:
        Next = cur.next
        cur.next = prev
        prev = cur
        cur = Next
    return prev  
```
## Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list/

```python
def middleNode(self, head: ListNode) -> ListNode:
    one = head
    two = head
    while (two != None) and (two.next != None):
        one = one.next
        if two.next == None:
            two = two.next
        else:
            two = two.next.next
    return one
```

## Palindrome Linked List

https://leetcode.com/problems/palindrome-linked-list/

```python
def isPalindrome(self, head: ListNode) -> bool:
    one = head
    two = head
    while (two != None) and (two.next != None):
        one = one.next
        if two.next == None:
            two = two.next
        else:
            two = two.next.next
    n = 0;
    sch = head;
    while sch != None:
        n = n + 1
        sch = sch.next
    if n%2 != 0:
        one = one.next
    cur = one
    Next = None
    prev = None
    while cur != None:
        Next = cur.next
        cur.next = prev
        prev = cur
        cur = Next
    one = prev
    flag = 1
    while one != None:
        if head.val != one.val:
            flag = 0
        head = head.next
        one = one.next
    return flag
```