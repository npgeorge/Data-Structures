# TODO a class that represents the individual elements

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        # what attributes do we need
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        # create a new Node
        new_node = Node(value)

        # check if list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # set next_node of my new Node to the head
            new_node.set_next_node(self.head)
            # update head attribute
            self.head = new_node
        
        # how do we know if the linked list only has a single element?
        
        # --- got this mixed up with something else ----
        #elif self.head == self.tail:
            # create a new node
            #new_node = Node(value)
            #update its pointer
            #new_node.set_next_node(self.head)
            # update head
            #self.head = new_node

        #else:
            # 1. create a new node
            #new_node = Node(-1)
            # 2. set next_node of my new node to the head
            #new_node.set_next_node(self.head)
            # 3. update the head attribute to replace previous head
            #self.head = new_node


    def add_to_tail(self, value):
        # create a new Node
        new_node = Node(value)
        # 1. List is empty
        if self.head is None:
            # update head & tail attributes
            self.head = new_node
            self.tail = new_node

        # 2. List is NOT empty
        else:
            # update next_node of our tail
            self.tail.set_next_node(new_node)
            # update self.tail
            self.tail = new_node

    
    def remove_head(self):
        # start with an empty list
        if self.head is None:
            return None
        # else, return VALUE of the old head
        else:
            return_value = self.head.get_value()
            # list with 1 element
            if self.head == self.tail:
                self.head = None
                self.tail = None
            # list with +2 elements
            else:
                self.head = self.head.get_next_node()
            return return_value

    def remove_tail(self):
        # empty list?
        if self.head is None:
            return None
        
        return_value = self.tail.get_value()
        # list with 1 element?
        if self.head == self.tail:
            # update head & tail attributes = None
            self.head = None
            self.tail = None
            return return_value
        
        # list with +2 elements?
        else:
            current_node = self.head
            while current_node.get_next_node() is not self.tail:
                current_node = current_node.get_next_node()
            # save value of tail
            # update the pointer of prev_tail
            # update the pointer of temp node (prev_tail) to None
            current_node.set_next_node(None)
            self.tail = current_node
            
            return return_value

    def contains(self, value):
        # loop through LL until next pointer is None
        current_node = self.head
        while current_node is not None:
            # if we find value
            if current_node.get_value() == value:
                return True
        
        # thing I was looking for was not in my LL
        return False

    def get_max(self):
        pass


    