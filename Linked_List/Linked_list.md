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
