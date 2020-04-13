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

if __name__ == "__main__":
    tree = SearchBinaryTree()
    tree.fillTree()

    tree.printTree()    


    