严格定义下BST中是没有值相等的节点的(No duplicate nodes)。
根据上述特性，我们可以得到一个结论：BST中序遍历得到的序列是升序的

## 基本操作之查找(Retrieve)

```Python

def searchBST(root, val):
    if not root:
        return None # 未找到值为val的节点
    if val < root.val:
        return searchBST(root.left, val) # val小于根节点值，在左子树中查找哦
    elif val > root.val:
        return searchBST(root.right, val) # val大于根节点值，在右子树中查找
    else:
        return root
```

## 基本操作之修改(Update)

修改仅仅需要在查找到需要修改的节点之后，更新这个节点的值就可以了，(假如修改过后整棵树还满足BST的性质)

```Python
def updateBSTBST(root, target, val):
    if not root:
        return  # 未找到target节点
    if target < root.val:
        updateBST(root.left, target, val) # target小于根节点值，在左子树中查找哦
    elif target > root.val:
        updateBST(root.right, target, val) # target大于根节点值，在右子树中查找
    else:  # 找到了
        root.val = val
```

## 基本操作之增加(Create)
根节点为空，则待添加的节点为根节点     
如果待添加的节点值小于根节点，则在左子树中添加     
如果待添加的节点值大于根节点，则在右子树中添加     
我们统一在树的叶子节点(Leaf Node)后添加     

```Python
def insertNode(root, node):
    if not root:
        return node
    if root.val > node.val:
        root.left = insertNode(root.left, node)
    else:
        root.right = insertNode(root.right, node)
    return root
```
## 基本操作之删除(Delete) （不要求掌握）
考虑待删除的节点为叶子节点，可以直接删除并修改父亲节点(Parent Node)的指针，需要区分待删节点是否为根节点。
考虑待删除的节点为单支节点(只有一棵子树——左子树 or 右子树)，与删除链表节点操作类似，同样的需要区分待删节点是否为根节点。
考虑待删节点有两棵子树，可以将待删节点与左子树中的最大节点进行交换，由于左子树中的最大节点一定为叶子节点，所以这时再删除待删的节点可以参考第一条。
详细的解释可以看 http://www.algolist.net/Data_structures/Binary_search_tree/Removal

```Python
def removeNode(root, value):
    dummy = TreeNode(0)
    dummy.left = root
    parent = findNode(dummy, root, value)
    node = None
    if parent.left and parent.left.val == value:
        node = parent.left
    elif parent.right and parent.right.val == value:
        node = parent.right
    else:
        return dummy.left
    deleteNode(parent, node)
    return dummy.left

def findNode(parent, node, value):
    if not node:
        return parent
    if node.val == value:
        return parent
    if value < node.val:
        return findNode(node,node.left, value)
    else:
        return findNode(node, node.right, value)

def deleteNode(parent, node):
    if not node.right:
        if parent.left == node:
            parent.left = node.left
        else:
            parent.right = node.left
    else:
        temp = node.right
        father = node
        while temp.left:
            father = temp
            temp = temp.left
        if father.left == temp:
            father.left = temp.right
        else:
            father.right = temp.right
        if parent.left == node:
            parent.left = temp
        else:
            parent.right = temp
        temp.left = node.left
        temp.right = node.right
```
