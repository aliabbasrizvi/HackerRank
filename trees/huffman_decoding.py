import Queue


class Node:
  def __init__(self, freq, data):
    self.freq = freq
    self.data = data
    self.left = None
    self.right = None


def huffman_hidden():  # builds the tree and returns root
  q = Queue.PriorityQueue()

  for key in freq:
    q.put((freq[key], key, Node(freq[key], key)))

  while q.qsize() != 1:
    a = q.get()
    b = q.get()
    obj = Node(a[0] + b[0], '\0')
    obj.left = a[2]
    obj.right = b[2]
    q.put((obj.freq, obj.data, obj))

  root = q.get()
  root = root[2]  # contains root object
  return root


def dfs_hidden(obj, already):
  if (obj == None):
    return
  elif (obj.data != '\0'):
    code_hidden[obj.data] = already

  dfs_hidden(obj.right, already + "1")
  dfs_hidden(obj.left, already + "0")


"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
def get_next_char(root, s, current_index):
  if current_index == len(s):
    return root.data, current_index

  if root.left is None and root.right is None:
    return root.data, current_index

  if s[current_index] == '0':
    return get_next_char(root.left, s, current_index + 1)

  if s[current_index] == '1':
    return get_next_char(root.right, s, current_index + 1)

def decodeHuff(root, s):
  # Enter Your Code Here
  current_idx = 0
  decoded_string = ''
  while current_idx < len(s):
    next_char, current_idx = get_next_char(root, s, current_idx)
    decoded_string += next_char

  print(decoded_string)


ip = raw_input()