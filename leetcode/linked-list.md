# linked-list

+ [Reverse Linked List](#reverse-linked-list)
+ [Middle of the Linked List](#middle-of-the-Linked-List)
+ [Palindrome Linked List](#palindrome-linked-list)
+ [Merge Two Sorted Lists](#merge-two-sorted-lists)
+ [Remove Nth Node From End of List](#remove-nth-node-from-end-of-list)
+ [Linked List Cycle II](#linked-list-cycle-II)
+ [Linked List Cycle](#linked-list-cycle)

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
    sorted_list = ListNode()
    cur = sorted_list    
    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next       
    if l1 is None:
        cur.next = l2
    if l2 is None:
        cur.next = l1   
    return sorted_list.next
```

## Remove Nth Node From End of List


https://leetcode.com/problems/remove-nth-node-from-end-of-list/

```python
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    cur = head
    sch = 0
    while cur is not None:
        sch += 1
        cur = cur.next            
    cur = head
    if cur.next is None:
        return None        
    for i in range(n):
        if cur.next is not None:
            cur = cur.next         
    cur2 = head.next
    prev = head
    while cur.next is not None:
        cur = cur.next
        cur2 = cur2.next
        prev = prev.next
    prev.next = prev.next.next
    if sch is n:
        return cur2
    return head    
```

## Linked List Cycle II


https://leetcode.com/problems/linked-list-cycle-ii/

```python
def detectCycle(self, head: ListNode) -> ListNode:
    s = head
    f = head
    while f and f.next:
        f = f.next.next
        s = s.next
        if f == s:
            f = head
            while f is not s:
                f = f.next
                s = s.next
            return s
    return None  
```

## Linked List Cycle


https://leetcode.com/problems/linked-list-cycle/

```python
def hasCycle(self, head: ListNode) -> bool:
    s = head
    f = head
    while f and f.next:
        f = f.next.next
        s = s.next
        if f == s:
            return 1
    return 0
```