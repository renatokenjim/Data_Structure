"""
LinkedIn Learning Course: 
Python Data Structures: Trees
https://www.linkedin.com/learning/python-data-structures-trees
"""

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

  def search(self, target):
    if self.data == target:
      print("Found it!")
      return self
    if self.left and self.data > target:
      return self.left.search(target)
    if self.right and self.data < target:
      return self.right.search(target)
    print("Value is not in tree")
  
  def traversePreorder(self):
    if self.left:
      self.left.traversePreorder()
    if self.right:
      self.right.traversePreorder()
  def traverseInorder(self):
    if self.left:
      self.left.traverseInorder()
    if self.right:
      self.right.traverseInorder() 
  def traversePostorder(self):
    if self.left:
      self.left.traversePostorder()
    if self.right:
      self.right.traversePostorder()
  
  def height(self, h=0):
    leftHeight = self.left.height(h+1) if self.left else h
    rightHeight = self.right.height(h+1) if self.right else h
    return max(leftHeight, rightHeight)

  def getNodesAtDepth(self, depth, nodes=[]):
    if depth==0:
      nodes.append(self.data)
      return nodes
    if self.left:
      self.left.getNodesAtDepth(depth-1, nodes)
    if self.right:
      self.right.getNodesAtDepth(depth-1, nodes)
    return nodes

class Tree:
  def __init__(self, root, name=''):
    self.root = root
    self.name = name
  def search(self, target):
    return self.root.search(target)
  def traversePreeorder(self):
    self.root.traversePreorder()
  def traverseInorder(self):
    self.root.traverseInorder()
  def traversePostorder(self):
    self.root.traversePostorder()
  def height(self):
    return self.root.height()
  def getNodesAtDepth(self, depth):
    return self.root.getNodesAtDepth(depth)
  
  def _nodeToChar(self, h, spacing):
    if n in None:
      return '_'+(' '*spacing)
    spacing = spacing-len(str(n))+1
    return str(n)+(' '*spacing)
    
  def print(self, label=''):
    print(self.name+''+label)
    height = self.root.height()
    spacing = 3
    width = int((2*height-1) * (spacing+1) +1)    # amount of spaces
    # Root offset
    offset = int((width-1)/2)
    for depth in range(0, height+1):
      if depth > 0:
        # print directional lines
        print(' '*(offset+1) + (' '*(spacing+2)).join(['/' + (' '*(spacing-2)) + '\\']*(2**(depth-1))))
      row = self.root.getNodesAtDepth(depth, [])
      print((' '*offset) + ''.join([self._nodeToChar(n, spacing) for n in row]))
      spacing = offset+1
      offset = int(offset/2) -1
    print('')
        

node = Node(10)
node.left = Node(5)
node.right = Node(15)

node.left.left = Node(2)
node.left.right = Node(6)

node.right.left = Node(13)
node.right.right = Node(10000)

myTree = Tree(node, '')


