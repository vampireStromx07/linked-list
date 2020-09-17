# program for linked list
# SinglyLinkedList


class node:         # this will create a node
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None           # this will be head node
        self.numOfNodes = 0        # this variable shows the sizes of linked list

    def insert_first(self, data):  # To insert node at the start
        new_node = node(data)      # this create a node

        if self.head is None:      # check the head is empty or not
            self.head = new_node
            self.numOfNodes += 1

        else:
            new_node.next = self.head
            self.head = new_node
            self.numOfNodes += 1

    def insert_end(self, data):    # to create a node at the end
        new_node = node(data)

        if self.head is None:
            self.head = new_node
            self.numOfNodes += 1

        else:
            temp = self.head
            while temp.next is not None:  # temp node now reaches to the last node
                temp = temp.next

            temp.next = new_node
            self.numOfNodes += 1


    def insert_at_pos(self, data, pos):
        new_node = node(data)

        if self.head is None:
            self.head = new_node

        else:
            count = self.numOfNodes
            if 1 <= pos <= count:     # check the position is valid or not
                self.numOfNodes += 1
                if pos == 1:
                    self.insert_first(data)

                elif pos == count:
                    self.insert_end(data)

                else:
                    temp = self.head
                    i = 1

                    while i < pos-1:          # now to temp node reaches the nth position (n = pos -1)
                        temp = temp.next
                        i += 1
                    new_node.next = temp.next
                    temp.next = new_node

            else:
                print(f"There are {count} nodes in the list.\n "
                      "Enter a valid position\n")

    def remove_first(self):

        if self.head is None:
            print("There are no nodes in the list.\n")  # check the list is empty or not.

        elif self.head.next is None:  # Only one node is present
            self.head = None

        else:
            temp = self.head                            # to delete the head node we use temp node
            self.head = self.head.next
            del temp
            self.numOfNodes -= 1

    def remove_end(self):

        if self.head is None:
            print("There are no nodes in the list.\n")

        elif self.head.next is None:  # Only one node is present
            self.head = None

        else:
            temp = self.head        # first we have to reach the last node
            prev_node = None        # previous node is used to delete the next link of last node

            while temp.next is not None:
                prev_node = temp
                temp = temp.next

            prev_node.next = None
            del temp                # delete the last node
            self.numOfNodes -= 1

    def remove_with_data(self, data):

        temp = self.head
        prev_node = None

        if self.head is None:
            return

        while temp is not None and temp.data != data:   # we are comparing data with node data
            prev_node = temp
            temp = temp.next

        if temp is None:      # it means we could not found the element because last node pointer is null
            return

        self.numOfNodes -= 1
        if prev_node is None:   # it means there are only one node present at a time
            self.head = temp.next

        else:
            prev_node.next = temp.next

    def Traverse(self):

        if self.head is None:
            print("LIST IS EMPTY.\n")

        else:
            temp = self.head

            while temp is not None:
                print(f"{temp.data} -->", end='')
                temp = temp.next


if __name__ == '__main__':

    SLL = SinglyLinkedList()

    while True:
        print("\n<-- Singly Linked List -->\n"
              "1. Insert_At_Start\n"
              "2. Insert_At_End\n"
              "3. Insert_At_Pos\n"
              "4. Remove_From_Start\n"
              "5. Remove_From_End\n"
              "6. Remove_With_Data\n"
              "7. Display_List\n"
              "8. Exit\n")

        print("Enter a choice: ", end='')
        choice = int(input())

        if choice == 1:
            a = input("Enter a data: ")
            SLL.insert_first(a)
            print("\n")

        if choice == 2:
            a = input("Enter a data: ")
            SLL.insert_end(a)
            print('\n')

        if choice == 3:
            a = input("Enter a data: ")
            b = int(input("Enter a position"))
            SLL.insert_at_pos(a, b)

        if choice == 4:
            SLL.remove_first()

        if choice == 5:
            SLL.remove_end()

        if choice == 6:
            a = input("Enter Data: ")
            SLL.remove_with_data(a)

        if choice == 7:
            SLL.Traverse()

        if choice == 8:
            exit()




