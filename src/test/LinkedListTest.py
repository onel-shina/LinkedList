import unittest
from LinkedList import LinkedList, Node


class MyTestCase(unittest.TestCase):
    def test_init(self):
        node3 = Node("Node 3")
        node2 = Node("Node 2")
        node1 = Node("Node 1")

        node1.next = node2
        node2.next = node3

        linked_list = LinkedList()
        linked_list.head = node1

        assert linked_list.head == node1
        assert linked_list.head.next == node2
        assert linked_list.head.next.next == node3
        assert linked_list.head.next.next.next is None

    def test_to_list(self):
        node3 = Node("Node 3")
        node2 = Node("Node 2")
        node1 = Node("Node 1")

        node1.next = node2
        node2.next = node3

        linked_list = LinkedList()
        linked_list.head = node1

        assert linked_list.to_list() == [node1.value, node2.value, node3.value]

    def test_to_list_empty(self):
        linked_list = LinkedList()
        assert linked_list.to_list() == []

    def test_prepend(self):
        linked_list = LinkedList()
        linked_list.prepend("Hello")
        linked_list.prepend("World")
        linked_list.prepend(",")
        linked_list.prepend("Python is Awesome")

        assert linked_list.to_list() == ["Python is Awesome", ",", "World", "Hello"]
        assert linked_list.size() == 4

    def test_prepend_1000_nodes(self):
        linked_list = LinkedList()
        inpt = []
        for i in range(0, 1000):
            linked_list.prepend(i)
            inpt.append(i)

        inpt.sort(reverse=True)
        assert linked_list.to_list() == inpt
        assert linked_list.size() == len(inpt)

    def test_append(self):
        linked_list = LinkedList()
        inpt = []
        for i in range(0, 1000):
            linked_list.append(i)
            inpt.append(i)

        inpt.sort()
        assert linked_list.to_list() == inpt
        assert linked_list.size() == len(inpt)

    def test_prepend_None(self):
        linked_list = LinkedList()
        linked_list.prepend(None)
        linked_list.prepend(None)

        assert linked_list.to_list() == [None, None]
        assert linked_list.size() == 2

    def test_append_None(self):
        linked_list = LinkedList()
        linked_list.append(None)
        linked_list.append(None)

        assert linked_list.to_list() == [None, None]
        assert linked_list.size() == 2

    def test_append_list(self):
        linked_list = LinkedList()
        inpt = ["Hello", "World", "Python is Awesome!"]
        linked_list.append_list(inpt)

        assert linked_list.to_list() == inpt
        assert linked_list.size() == len(inpt)

    def test_append_list(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)

        linked_list.append_list(["Hello", "World", "Python is Awesome!"])

        assert linked_list.to_list() == [1, 2, 3, "Hello", "World", "Python is Awesome!"]
        assert linked_list.size() == 6

    def test_append_empty_list(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)

        linked_list.append_list([])

        assert linked_list.to_list() == [1, 2, 3]
        assert linked_list.size() == 3

    def test_append_none_list(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)

        linked_list.append_list(None)

        assert linked_list.size() == 3
        assert linked_list.to_list() == [1, 2, 3]

    def test_remove_empty(self):
        linked_list = LinkedList()
        linked_list.remove(1)

        assert linked_list.size() == 0
        assert linked_list.to_list() == []

    def test_remove_None(self):
        linked_list = LinkedList()
        inpt = [None, None]
        linked_list.append_list(inpt)
        linked_list.remove(None)

        assert linked_list.size() == len(inpt) - 1
        assert linked_list.to_list() == [None]

    def test_remove_first_element(self):
        linked_list = LinkedList()
        inpt = ["Hello", "World", "Python", "Is", "Awesome"]
        linked_list.append_list(inpt)
        linked_list.remove(inpt[0])

        assert linked_list.size() == len(inpt) - 1
        assert linked_list.to_list() == inpt[1:]

    def test_remove_middle_element(self):
        linked_list = LinkedList()
        inpt = ["Hello", "World", "Python", "Is", "Awesome"]
        linked_list.append_list(inpt)
        linked_list.remove(inpt[2])

        assert linked_list.size() == len(inpt) - 1
        assert linked_list.to_list() == inpt[:2] + inpt[3:]

    def test_remove_last_element(self):
        linked_list = LinkedList()
        inpt = ["Hello", "World", "Python", "Is", "Awesome"]
        linked_list.append_list(inpt)
        linked_list.remove(inpt[-1])

        assert linked_list.size() == len(inpt) - 1
        assert linked_list.to_list() == inpt[:-1]

    def test_remove_non_existing_element(self):
        linked_list = LinkedList()
        inpt = ["Hello", "World", "Python", "Is", "Awesome"]
        linked_list.append_list(inpt)
        linked_list.remove("hi")

        assert linked_list.size() == len(inpt)
        assert linked_list.to_list() == inpt

    def test_pop_empty(self):
        linked_list = LinkedList()
        assert linked_list.to_list() == []
        assert linked_list.size() == 0

    def test_pop_one_element(self):
        linked_list = LinkedList()
        linked_list.append("Hello")
        assert linked_list.pop() == "Hello"
        assert linked_list.size() == 0

    def test_pop_100_elements(self):
        linked_list = LinkedList()
        inpt = list(range(0, 100, 1))
        output = []
        linked_list.append_list(inpt)
        for i in range(len(inpt)):
            output.append(linked_list.pop())

        assert inpt == output
        assert linked_list.size() == 0

    def test_search_empty(self):
        linked_list = LinkedList()
        assert linked_list.search(1) is False

    def test_search_first_element(self):
        linked_list = self.make_hundred_elements_linked_list()
        assert linked_list.search(1) is True

    def test_search_middle_element(self):
        linked_list = self.make_hundred_elements_linked_list()
        assert linked_list.search(50) is True

    def test_search_last_element(self):
        linked_list = self.make_hundred_elements_linked_list()
        assert linked_list.search(100) is True

    def test_search_non_existing_element(self):
        linked_list = self.make_hundred_elements_linked_list()
        assert linked_list.search(101) is False

    def test_insert_empty_list(self):
        linked_list = LinkedList()
        linked_list.insert("Hello", 0)
        assert linked_list.to_list() == ["Hello"]
        assert linked_list.size() == 1

    def test_insert_empty_list_index3(self):
        linked_list = LinkedList()
        linked_list.insert("Hello", 3)
        assert linked_list.to_list() == ["Hello"]
        assert linked_list.size() == 1


    def test_insert_empty_list_index100(self):
        linked_list = LinkedList()
        linked_list.insert("Hello", 100)
        assert linked_list.to_list() == ["Hello"]
        assert linked_list.size() == 1


    def test_insert_first(self):
        linked_list, inpt = self.make_five_elements_linked_list()
        linked_list.insert("Hello", 0)
        assert linked_list.to_list() == ["Hello"] + inpt
        assert linked_list.size() == len(inpt) + 1

    def test_insert_last(self):
        linked_list, inpt = self.make_five_elements_linked_list()
        linked_list.insert("Hello", len(inpt))
        assert linked_list.to_list() == inpt + ["Hello"]
        assert linked_list.size() == len(inpt) + 1

    def test_insert_middle(self):
        linked_list, inpt = self.make_five_elements_linked_list()
        index_to_insert = 2
        linked_list.insert("Hello", index_to_insert)
        assert linked_list.to_list() == inpt[:index_to_insert] + ["Hello"] + inpt[index_to_insert:]
        assert linked_list.size() == len(inpt) + 1


    def make_hundred_elements_linked_list(self):
        linked_list = LinkedList()
        linked_list.append_list(list(range(1, 101, 1)))
        return linked_list

    def make_five_elements_linked_list(self):
        linked_list = LinkedList()
        inpt = list(range(1, 6, 1))
        linked_list.append_list(inpt)  # [1,2,3,4,5]
        return linked_list, inpt


if __name__ == '__main__':
    unittest.main()
