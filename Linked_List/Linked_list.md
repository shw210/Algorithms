## 83. Remove Duplicates from Sorted List
```Python
class Solution(object):
    def deleteDuplicates(self, head):
       current = head 
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
                
        return head
```
## 19. Remove Nth Node From End of List
思路：因为linked list不容易知道它的size，所以我们必须用 two pointer 的方法找到倒数第 n 个 node 是哪个       
注意：不要return head, 因为 head 本身也有可能是那个被去除的Node

```Python
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(val = 0, next = head)
        fast, slow = dummy, dummy
        
        i = 0
        while i <= n:
            fast = fast.next
            i += 1
            
        while fast:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        
        return dummy.next

```
