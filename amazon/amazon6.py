'''
linked lists
'''

class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.root = Node()

    def append(self,value):
        if self.root.next is None:
            self.root.next = Node(value)
            return
        else:
            cur_node = self.root.next
            while cur_node.next is not None:
                cur_node = cur_node.next
            cur_node.next = Node(value)

    def display(self):
        print(self.getElements())
        return

    def displayReverse(self):
        elems = self.getElements()
        elems.reverse()
        print(elems)

    def getElements(self):
        if self.root.next is None:
            return []
        else:
            cur_node = self.root.next
            elems = []
            while cur_node is not None:
                elems.append(cur_node.data)
                cur_node = cur_node.next
            return elems

    def length(self):
        if self.root.next is None:
            return 0
        else:
            cur_node = self.root.next
            length = 0
            while cur_node is not None:
                length += 1
                cur_node = cur_node.next
            return length

    def get(self, index):
        if index < 0 or index >= self.length():
            print('ERROR: "Get" index out of range')
            return None
        elif self.root.next is None:
            print('ERROR: list is empty')
            return None
        else:
            cur_node = self.root.next
            for _ in range(index):
                cur_node = cur_node.next
            return cur_node.data

    def erase(self, index):
        if index < 0 or index >= self.length():
            print('ERROR: "Erase" index out of range')
            return 
        elif self.root.next is None:
            print('ERROR: list is empty')
            return 
        else:
            prev_node = None
            cur_node = self.root.next
            for _ in range(index):
                prev_node = cur_node
                cur_node = cur_node.next
            prev_node.next = cur_node.next
            return
    
    def __getitem__(self,index):
        return self.get(index)

    def insert(self, value, index):
        if index < 0:
            print('ERROR: "Insert" index cannot be negative')
            return False
        elif index >= self.length():
            return self.append(value)
        else:
            prev_node = self.root
            cur_node = self.root.next
            idx = 0
            while True:
                if idx == index:
                    new_node = Node(value)
                    prev_node.next = new_node
                    new_node.next = cur_node
                    return True
                idx+=1
                prev_node = cur_node
                cur_node = cur_node.next

    def set(self, value, index):
        if index < 0:
            print('ERROR: "Set" index cannot be negative')
            return False
        elif index >= self.length():
            print('ERROR: "Set" index out of bounds')
            return False
        else:
            cur_node = self.root.next
            idx = 0
            while True:
                if idx == index:
                    cur_node.data = value
                    return True
                idx+=1
                cur_node = cur_node.next

    def setLastPointer(self):
        length = self.length()
        idx = 0
        cur_node = self.root
        while True:
                if idx == length-1:
                    cur_node.next = self.root.next
                    return True
                idx+=1
                cur_node = cur_node.next

    def detectCycle(self):
        if self.root is None:
            return False
        cur_node = self.root
        ids = []
        while True:
            if cur_node is None:
                return False
            if id(cur_node) in ids:
                return True
            ids.append(id(cur_node))
            cur_node = cur_node.next

    def copy(self):
        newList = LinkedList()
        if self.root is None:
            print('ERROR: "Copy" list is empty')
            return None
        elif self.root.next is None:
            return newList
        else:
            curNode = self.root.next
            while True:
                if curNode is None:
                    return newList
                newList.append(curNode.data)
                curNode = curNode.next

    def merge(self, list2):
        # case 1 - both lists are empty
        if self.root is None and list2.root is None:
            return LinkedList()
        # case 2 - list1 is empty
        elif self.root is None and list2.root is not None:
            return list2.copy()
        # case 3 - list2 is empty
        elif self.root is not None and list2.root is None:
            return self.copy()
        # case 4 - lists are not empty
        else:
            elems = self.getElements()
            elems = elems + list2.getElements()
            elems.sort()
            mergedList = LinkedList()
            for x in elems:
                mergedList.append(x)
            return mergedList

myList = LinkedList()

myList.append(10)
myList.append(11)
myList.append(12)
myList.append(13)
myList.append(14)

myList2 = myList.copy()
merged = myList.merge(myList2)

myList.display()
myList2.display()
merged.display()

# print(id(myList))
# print(id(myList2))
# print(id(merged))

# print('Length = ' + str(myList.length()))

# myList.insert(2,4)
# myList.display()
# myList.set(2000, 4)
# myList.display()
# myList.setLastPointer()
# print(myList.detectCycle())