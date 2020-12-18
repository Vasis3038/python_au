# linked-list

+ [Reverse Linked List](#reverse-linked-list)
+ [Middle of the Linked List](#middle-of-the-Linked-List)
+ [Palindrome Linked List](#palindrome-linked-list)
+ [Merge Two Sorted Lists](#merge-two-sorted-lists)

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

## Merge Two Sorted Lists


https://leetcode.com/problems/merge-two-sorted-lists/

```python
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if not l1: 
        return l2
    if not l2: 
        return l1
    if l1.val < l2.val:
        left, right = l1, l2 
    else:
        left, right = l2, l1
    res = left
    while left.next and right:
        if right.val < left.next.val:
            temp = right.next
            right.next = left.next
            left.next = right
            right = temp
        left = left.next   
    if right:
        left.next = right
    return res
```