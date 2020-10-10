# linked-list

+ [Reverse Linked List](#reverse-linked-list)

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
