class ListNode:
    def __init__(self, val, next=None):
        self.next = next
        self.val = val

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0
    
    def get(self, index: int) -> int:
        if self.num_elements == 0 or index >= self.num_elements:
            return -1
        current_index, current_node = 0, self.head
        while current_node:
            if current_index == index:
                return current_node.val
            current_index += 1
            current_node = current_node.next
        return -1

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)
        if self.num_elements == 0:
            self.head = newNode
            self.tail = self.head
        else:
            newNode.next = self.head
            self.head = newNode
        self.num_elements += 1

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)
        if self.num_elements == 0:
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.num_elements += 1

    def remove(self, index: int) -> bool:
        if self.num_elements == 0 or index >= self.num_elements:
            return False
        prev_node, current_index, current_node = None ,0, self.head
        while current_node:
            if current_index == index:
                #delete node
                if current_index == 0:
                    self.head = current_node.next
                    if self.head is None:
                        self.tail = None
                else:
                    prev_node.next = current_node.next
                    if current_node == self.tail:
                        self.tail = prev_node 
                self.num_elements -= 1
                return True
            current_index += 1
            prev_node = current_node
            current_node = current_node.next
        return False


    def getValues(self) -> List[int]:
        currentNode = self.head
        arr = []
        while currentNode:
            arr.append(currentNode.val)
            currentNode = currentNode.next
        return arr