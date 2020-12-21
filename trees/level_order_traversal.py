class Node:
  def __init__(self, info):
    self.info = info
    self.left = None
    self.right = None
    self.level = None

  def __str__(self):
    return str(self.info)


class BinarySearchTree:
  def __init__(self):
    self.root = None

  def create(self, val):
    if self.root == None:
      self.root = Node(val)
    else:
      current = self.root

      while True:
        if val < current.info:
          if current.left:
            current = current.left
          else:
            current.left = Node(val)
            break
        elif val > current.info:
          if current.right:
            current = current.right
          else:
            current.right = Node(val)
            break
        else:
          break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

def set_level_order(processed, order):
  if len(processed) == 0:
    return
  node = processed.pop(0)
  order.append(str(node.info))

  if node.left:
    processed.append(node.left)

  if node.right:
    processed.append(node.right)

  set_level_order(processed, order)


def levelOrder(root):
  processed = []
  if root:
    processed.append(root)

  order = []
  set_level_order(processed, order)
  print(' '.join(order))
