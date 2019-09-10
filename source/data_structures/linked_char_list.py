from source.data_structures.linked_list import LinkedList


class LinkedCharList(LinkedList):
    """
        A Linked list of characters.
    """

    CHARACTERS_ = ["\n", "\t"]
    
    def clean_blankspaces(self):
        """
            Removes excess of blank spaces in strings.
        """
        field = self.head
        while field.next is not None:
            if field.data == " " and field.next.data == " ":
                aux = field.next.next
                field.next = aux
                aux = None
            elif field.next is not None:
                field = field.next    

        self.head.next = self.head.next.next if self.head.next.data == " " else self.head.next

    def clean(self):
        """
            Removes \n and \t from strings.
        """
        field = self.head
        while field.next is not None:
            if field.data in self.CHARACTERS_:
                field.data = " "                
            if field.next is not None:
                field = field.next

    def to_list(self):
        return [character for character in self]
        
    def to_string(self):
        return "".join(self.to_list()).strip()

