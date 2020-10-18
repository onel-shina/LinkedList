class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.__size = 0

    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """

        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.__size += 1

    def append(self, value):
        """ Append a value to the end of the list. """

        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = node
        self.__size += 1

    def append_list(self, lst):
        """ Constructs a linked list from list, if linked list is not empty then it appends the list to the end. """

        if isinstance(lst, list):
            if len(lst) == 1:
                self.append(lst[0])

            elif len(lst) > 1:
                if self.head is None:
                    self.head = Node(lst[0])
                    self.__size += 1
                    current_node = self.head
                    for item in lst[1:]:
                        current_node.next = Node(item)
                        self.__size += 1
                        current_node = current_node.next
                else:
                    current_node = self.head
                    while current_node.next:
                        current_node = current_node.next
                    for item in lst:
                        current_node.next = Node(item)
                        self.__size += 1
                        current_node = current_node.next

    def remove(self, value):
        """ Remove first occurrence of value. """

        if self.size() > 0:
            if self.head.value == value:
                self.head = self.head.next
                self.__size -= 1
            else:
                current_node = self.head
                while current_node.next:
                    if current_node.next.value == value:
                        current_node.next = current_node.next.next
                        self.__size -= 1
                        break
                    current_node = current_node.next

    def pop(self):
        """ Return the first node's value and remove it from the list. """
        if self.head:
            node = self.head
            self.head = self.head.next
            self.__size -= 1
            return node.value

    def size(self):
        """ Return the size or length of the linked list. """
        return self.__size

    def search(self, value):
        """ Search the linked list for a node with the requested value and
        returns true if it exists otherwise returns false. """

        result = False
        current_node = self.head
        while current_node:
            if current_node.value == value:
                result = True
                break
            else:
                current_node = current_node.next
        return result

    def to_list(self):
        """ Returns a list object from the linked list. """

        lst = []
        current_node = self.head
        while current_node:
            lst.append(current_node.value)
            current_node = current_node.next

        return lst

    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
            length of the list, append to the end of the list. """

        if pos == 0:
            self.prepend(value)
        elif pos >= self.size():
            self.append(value)
        else:
            node = Node(value)
            iter_position = 0
            current_node = self.head
            while current_node.next:
                iter_position += 1
                if iter_position == pos:
                    node.next = current_node.next
                    current_node.next = node
                    break
                current_node = current_node.next
            self.__size += 1
