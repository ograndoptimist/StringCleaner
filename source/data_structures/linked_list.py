"""
    Baseline data structures.
"""


class Node(object):
    def __init__(self):
        self.next = None
        self.data = None
    

class LinkedList(object):
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.length = 0

    @staticmethod
    def __create_node(item):
        new_item = Node()
        new_item.next = None
        new_item.data = item
        return new_item

    def __extend_node(self):
        search = self.head.next
        while True:
            if search.next is not None:
                search = search.next
            else:
                return search        
    
    def build_nodes(self, items):
        items = list(items)
        for item in items:
            new_item = LinkedList.__create_node(item) 
            if self.length == 0:
                self.head.next = new_item
            else:
                search = self.__extend_node()
                search.next = new_item             
            self.tail.next = new_item
            self.length += 1

    def __iter__(self):
        search = self.head.next
        while search is not None:
            yield search.data
            search = search.next        
