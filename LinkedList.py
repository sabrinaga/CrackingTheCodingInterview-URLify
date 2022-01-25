#linked list is not a built in feature of python
# Linked lists store data in an ordered manner
class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def list_length(self):
        cur = self.head
        length = 0
        while cur.next != None:
            length += 1
            cur = cur.next
        return length

    def printList(self):
        nodeList = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            nodeList.append(cur_node.data)
        print(nodeList)

    def get(self, index):
        if index >= self.list_length():
            print("Error: Invalid Index! Index out of range!")
            return None
        cur_index = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_index == index:
                return cur_node.data
            cur_index += 1


if __name__ == '__main__':

    my_list = LinkedList()
    my_list.printList()
    my_list.append(1)
    my_list.append(2)
    my_list.append("element 3")
    my_list.append("element 4")
    my_list.printList()
    third_element = my_list.get(3)
    print("The third element is:", third_element) #Recall that indexing starts at 0
