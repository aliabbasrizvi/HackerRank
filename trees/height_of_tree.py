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


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''

def height(root):
  left_height = 0
  right_height = 0

  if root is None:
    return 0

  if root.left:
    left_height = 1 + height(root.left)

  if root.right:
    right_height = 1 + height(root.right)

  return max(left_height, right_height)
