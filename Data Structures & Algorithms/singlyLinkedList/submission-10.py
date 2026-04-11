class ListNode:
    def __init__(self, val, next=None):
        self.next = next
        self.val = val

class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        current_index, current_node = 0, self.head.next
        while current_node:
            if current_index == index:
                return current_node.val
            current_index += 1
            current_node = current_node.next
        return -1

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head.next
        self.head.next = newNode
        if not newNode.next:
            self.tail = newNode

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)
        self.tail.next = newNode
        self.tail = newNode

    def remove(self, index: int) -> bool:
        current_index, current_node = 0, self.head
        while current_node and current_index < index:
            current_index += 1
            current_node = current_node.next
        
        if current_node and current_node.next:
            if current_node.next == self.tail:
                self.tail = current_node
            current_node.next = current_node.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        currentNode = self.head.next
        arr = []
        while currentNode:
            arr.append(currentNode.val)
            currentNode = currentNode.next
        return arr