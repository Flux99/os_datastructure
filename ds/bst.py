from collections import deque

class Node:

  def __init__(self, val):
    self.left = None
    self.right = None
    self.val = val


class BST:

  def __init__(self):
    self.root = None

  def insert(self, root, val):
    if root is None:
      return Node(val)
    else:
      if root.val < val:
        root.right = self.insert(root.right, val)
      else:
        root.left = self.insert(root.left, val)
    return root

  def inordertraversal(self, root):
    if root:
      self.inordertraversal(root.left)
      print(root.val, end="->")
      self.inordertraversal(root.right)
   

  def postordertraversal(self, root):
    if root:
      self.postordertraversal(root.left)
      self.postordertraversal(root.right)
      print(root.val, end="->")
    else:
      # print("else")
      return

  def preordertraversal(self, root):
    if root:
      print(root.val, end="->")
      self.preordertraversal(root.left)
      self.preordertraversal(root.right)
    else:
      # print("else")
      return

  def findmini(self, root):
    if root is None:
      return False
    elif root.left is None:
      return root.val
    return self.findmini(root.left)

  def findheight(self, root):
    if root is None:
      return -1
    else:
      return max(self.findheight(root.left), self.findheight(root.right)) + 1

  def findlongestpath(self, root):
    if root is None:
      return 0
    else:
      return max(self.findheight(root.left), self.findheight(root.right)) + 1

  def level_order_traversal(self,root):
    if root is None:
      return

    queue = deque([root])
    while queue:
      curr = deque()
      level_size = len(queue)

    for _ in range(level_size):
        node = queue.popleft()
        curr.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print(" ".join(str(val) for val in curr))
      


bst = BST()

root = None

root = bst.insert(root, 100)

node1 = bst.insert(root, 115)

node2 = bst.insert(root, 120)
node3 = bst.insert(root, 150)

node4 = bst.insert(root, 90)

node5 = bst.insert(root, 70)
node6 = bst.insert(root, 50)
node7 = bst.insert(root, 10)

print("Inorder traversal of the BST:")
bst.inordertraversal(root)

print("Postorder traversal of the BST:")
bst.postordertraversal(root)

print("Preorder traversal of the BST:")
bst.preordertraversal(root)

minival = bst.findmini(root)
print('minival', minival)

longestpath = bst.findlongestpath(root)
print('longestpath', longestpath)

print()
bst.level_order_traversal(root)