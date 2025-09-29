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

  # Binary Search Tree seach: returns the node or None
  def search(self, target):
    if self.data == target:
      return self
    if self.left and self.data > target:
      return self.left.search(target)
    if self.right and self.data < target:
      return self.right.search(target)
    # print("Value is not in tree")
    return None

  def add(self, data):
    if self.data == data:
      return self
    if data < self.data:
      if self.left is None:
        self.left = Node(data)
      else:
        self.left.add(data)
    if data > self.data:
      if self.right is None:
        self.right - Node(data)
      else:
        self.right.add(data)
  
  def findMin(self):
    if self.left:
      return self.left.findMin()
    return self.data
      
  def delete(self,target):
    if self.data == target:
      if self.left and self.right:      # if one of either exists
        # RTFM
        minValue = self.right.findMin()
        self.data = minValue
        self.right = self.right.delete(minValue)
        return self
      else:
        return self.left or self.right
    if self.right and target > self.data:
      self.right = self.right.delete(target)
    if self.left and target < self.data:
      self.left = self.left.delete(target)
  
  def isBalanced(self):
    leftHeight = self.left.height()+1 if self.left else 0
    rightHeight = self.right.height()+1 if self.right else 0
    return abs(leftHeight - rightHeight) < 2
  def toStr(self):
    if not self.isBalanced():
      return str(self.data)+'*'
    return str(self.data)
    

  # these methods are just recursing left/right. They would be useful if they visited/printed/returned the current node.
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
  
  """
  Height as number of levels (nodes):
      Leaf node = height 1.  Path length from root to deepest leaf counting nodes.  --> add +1 to the max(left,right).
  Height as maximum edge count:
      Leaf node = height 0.  Path length from root to deepest leaf counting edges. 
  """
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
    else:
      left_list = [None] * (2 ** (depth - 1))
    if self.right:
      self.right.getNodesAtDepth(depth-1, nodes)
    else: right_list = [None] * (2 ** (depth - 1))
    return nodes


#===================================================================

class Tree:
  def __init__(self, root, name=''):
    self.root = root
    self.name = name
  def search(self, target):
    return self.root.search(target)
  def add(self, data):
    self.root.add(data)
  def traversePreorder(self):
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
    if n is None:
      return '_'+(' '*spacing)
    spacing = spacing-len(n.toStr())+1
    return n.toStr()+(' '*spacing)
    
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
  
  def delete(self,target):
    self.root = self.root.delete(target)    # return the new node put in place
  

node = Node(10)
node.left = Node(5)
node.right = Node(15)

node.left.left = Node(2)
node.left.right = Node(6)

node.right.left = Node(13)
node.right.right = Node(10000)

myTree = Tree(node, '')


