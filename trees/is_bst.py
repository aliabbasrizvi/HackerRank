""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""

def is_bst(root, min, max):
  if root is None:
    return True

  if min and root.data <= min:
    return False

  if max and root.data >= max:
    return False

  is_left_bst = is_bst(root.left, min, root.data)
  is_right_bst = is_bst(root.right, root.data, max)

  return is_left_bst and is_right_bst


def checkBST(root):
  if root is None:
    return False

  return is_bst(root, None, None)
