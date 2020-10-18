"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
import sys
sys.path.append('../stack')
sys.path.append('../queue')
from stack import Stack
from queue import Queue

class Stack:
    def __init__(self):
        self.stack = list()

    def __len__(self):
        return len(self.stack)

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # create new node
        new_node = BSTNode(value)

        if not self.value:
            self.value = value
        # if value is < new_node, insert left
        elif value < self.value:
            if not self.left:
                self.left = new_node
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = new_node
            else:
                self.right.insert(value)

        # if value is < root, insert left
        # check if next value is > or < or None
        # need to go down each level of the tree
        
        # if value < root, go left
        #if self.value is <= 
            # if right child is None
                # add here left child = BTSNode(value)
            # else
                #self.left.insert(value)
        
        # if value >= root, go right
            # if right child is None
                # add here
            # else
                #self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if self.value is target
        if self.value is target:
            return True # if yes, return True
        # if no
         # go left
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        # go right
        else:
            if self.right:
                return self.right.contains(target)
            else:
                return False


    # Return the maximum value found in the tree
    def get_max(self):
        # go right until you cannot anymore
        # while loop or recursively
        # then return value at far right
        # make sure you return the value and not the node there
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # how can I do this recursively?
        # do one side, then the other
        fn(self.value)

        # base case - no child nodes, do nothing

        # recursive case - one or more children
        # go left, call fn() for each node
        if self.left:
            self.left.for_each(fn)
        # go right, call fn() for each node
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            node.left.in_order_print(node.left)
        print(node.value)
        if node.right:
            node.right.in_order_print(node.right)
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # make queue
        queue = Queue()
        # enqueue the node
        queue.enqueue(node)
        # while loop - as long as Q is not empty
        while len(queue) != 0:
            current_node = queue.dequeue()
            print(current_node.value)
            if current_node.left:
                queue.enqueue(current_node.left)
            if current_node.right:
                queue.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # make a stack
        stack = Stack()
        # push node
        stack.push(node)
        # while loop - as long as the stack is not empty
        while len(stack) != 0:
            # pop off
            current_node = stack.pop()
            print(current_node.value)
            # put on stack
            if current_node.left:
                stack.push(current_node.left)
            if current_node.right:
                stack.push(current_node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

#bst.bft_print()
#bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
#bst.in_order_print()
print("post order")
bst.post_order_dft()  
