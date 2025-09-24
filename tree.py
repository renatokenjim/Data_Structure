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
    return self.roott.height()
    

node = Node(10)
node.left = Node(5)
node.right = Node(15)

node.left.left = Node(2)
node.left.right = Node(6)

node.right.left = Node(13)
node.right.right = Node(10000)

myTree = Tree(node, '')


