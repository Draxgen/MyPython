'''
Binary Search Tree
'''

import random

class Node():
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None

class SearchBinaryTree():
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
    
    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child is None:
                cur_node.left_child = Node(value)
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child is None:
                cur_node.right_child = Node(value)
            else:
                self._insert(value, cur_node.right_child)
        else:
            print('Value already exists!')
    
    def printTree(self):
        '''print left child, then current, then right child''' 
        if self.root is None:
            print('None')
        else:
            self._printNode(self.root)
    
    def _printNode(self, curNode):
        if curNode.left_child is not None: self._printNode(curNode.left_child)
        print(curNode.value)
        if curNode.right_child is not None: self._printNode(curNode.right_child)

    def fillTree(self):
        for _ in range(100):
            self.insert(random.randint(0,1000))

    def getHeight(self):
        if self.root is not None:
            height = self._getHeight(self.root)
        else:
            height = 0
        return height

    def _getHeight(self, node):
        leftHeight = 0
        rightHeight = 0
        if node.left_child is not None:
            leftHeight = self._getHeight(node.left_child) + 1
        else:
            leftHeight = 1 # if node has no children height of the node is 1 to count its own height
        if node.right_child is not None:
            rightHeight = self._getHeight(node.right_child) + 1
        else:
            leftHeight = 1 # if node has no children height of the node is 1 to count its own height
        return max(leftHeight, rightHeight)

    def getNumberOfNodes(self):
        if self.root is not None:
            num = self._getNumberOfNodes(self.root)
        else:
            num = 0
        return num

    def _getNumberOfNodes(self, node):
        if node.left_child is not None:
            left = self._getNumberOfNodes(node.left_child)
        else:
            left = 0
        if node.right_child is not None:
            right = self._getNumberOfNodes(node.right_child)
        else:
            right = 0
        return left+right+1

    def findNode(self, value):
        if self.root is not None:
            return self._findNode(value, self.root)
        else:
            return None
   
    def _findNode(self, value, node):
        if node.value == value:
            return node
        elif node.value > value:
            return self._findNode(value, node.left_child)
        elif node.value < value:
            return self._findNode(value, node.right_child)

    def deleteNode(self,value):
        toDelNode = self.findNode(value)
        if toDelNode is not None:
            self._deleteNode(toDelNode)
        else:
            print('Node to be deleted does not exist')

    def _deleteNode(self,node):
        leftChild, rightChild = self._getChildren(node)
        #case 1 - node has no children
        if leftChild is None and rightChild is None:

        #case 2 - node has only left child
        #case 3 - node has only right child
        #case 4 - node has both children

    def _getChildren(self,node)
        return node.left_child, node.right_child

    def _getPredecessorAndItsParent(self,node):
        if node.left_child

    def getParent(self,node):
        if node is self.root:
            return None
        elif self.root is not None:
            return self._getParent(node)
        else:
            return None
    
    def _getParent(self, node):
        if node.left_child == node:
            return node
        if node.right_child == node:
            return node
        left = self._getParent(node.left_child)
        right = self._getParent(node.right_child)
        if left is None and right is None:
            return None
        if left is not None and right is None:
            return left
        if left is None and right is not None:
            return right


if __name__ == "__main__":
    tree = SearchBinaryTree()
    tree.fillTree()

    tree.printTree()    

    print(tree.getHeight())
    print(tree.getNumberOfNodes())

    