import time
from contextlib import contextmanager
import gc

class Node:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value


class Tree:
    def __init__(self) -> None:
        self.root = None
        self.inorder = []

    def insert(self, value):
        Newnode = Node(value)
        if self.root is None:
            self.root = Newnode
        else:
            currentNode = self.root
            while (True):
                # Left
                if value < currentNode.value:
                    if currentNode.left is None:
                        currentNode.left = Newnode
                        return self
                    else:
                        currentNode = currentNode.left
                # Right
                else:
                    if currentNode.right is None:
                        currentNode.right = Newnode
                        return self
                    else:
                        currentNode = currentNode.right
        return self.root

    def lookup(self, value):
        currentNode = self.root
        while (currentNode):
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            elif value == currentNode.value:
                return currentNode
        return False

    def remove(self, key):
        curr = self.root
        prev = None
        while (curr):
            if key < curr.value:
                prev = curr
                curr = curr.left
            elif key > curr.value:
                prev = curr
                curr = curr.right
            elif key == curr.value:
                #if trg does not have any child
                if curr.left is None and curr.right is None:
                    if prev.left:
                        if prev.left.value == key:
                            prev.left = None
                        else: prev.right = None
                    else: prev.right = None
                    break

                #if trg have child
                else:
                    deep = 0
                    if len(self.inorder) == 0:
                        self.remove_helper(key)
                        get_index = self.inorder.index(key)
                        curr.value = self.inorder[get_index - 1]
                        deep += 1
                        curr = None
                    else:
                        deep += 1
                        get_index = self.inorder.index(key)
                        # curr.value = self.inorder[get_index - 1]
                        self.remove(self.inorder[get_index - 1])
                        curr.value = self.inorder[get_index - 1]
                        curr = None
        return self.root
    
    def online(self, key):
        curr = self.root
        prev = None
        while (curr != None and curr.value != key):
            prev = curr
            if curr.value < key:
                curr = curr.right
            else:
                curr = curr.left

        if curr is None:
            print("Key % d not found in\
           the provided BST." % key)
            return self.root
        
        if curr.left == None or curr.right == None:
            newcurr = None
            
            if curr.left is None:
                newcurr = curr.right
            else: newcurr = curr.left

            if prev is None:
                return newcurr
            
            if curr == prev.left:
                prev.left = newcurr
            else: prev.right = newcurr
            curr = None
        else:
            p = None
            temp = None
            temp = curr.right
            while(temp.left != None):
                p = temp
                temp = temp.left
            if p != None:
                p.left = temp.right
 
            else:
                curr.right = temp.right
            curr.value = temp.value
            temp = None

        return self.root

    def remove_helper(self, key):
        current = self.root
        stack = []
        ans = []
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif(stack):
                current = stack.pop()
                self.inorder.append(current.value)
                current = current.right
            else:
                break
        get_index = self.inorder.index(key)
        self.remove(self.inorder[get_index - 1])
        return self.inorder[get_index - 1]

    def Inorder(self):
        current = self.root
        stack = []
        ans = []
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif(stack):
                current = stack.pop()
                ans.append(current.value)
                current = current.right
            else:
                break
        return ans


tree = Tree()
# tree.insert(50)
# tree.insert(10)
# tree.insert(90)
# tree.insert(80)
# tree.insert(100)
# tree.insert(44)
# tree.insert(46)
# tree.insert(75)
# tree.insert(85)
# print(tree.remove(46))
tree.insert(1)
tree.insert(90)
tree.insert(100)
tree.insert(80)
tree.insert(85)
tree.insert(84)
tree.insert(83)
tree.insert(82)
tree.insert(81)
tree.insert(86)
tree.insert(70)
tree.insert(75)
tree.insert(60)
tree.insert(65)
tree.insert(50)
tree.insert(55)
tree.insert(40)

@contextmanager
def timer(lable:str):
    start: float = time.perf_counter()
    try:
        yield
    finally:
        end: float = time.perf_counter()
        print(f'{lable}: {end - start:3f} secs')

for i in range(1):
    gc.collect()
    # with timer("Jemish"):
    #     result = tree.remove(80)
    with timer("Online"):
        result = tree.online(80)
    time.sleep(1)