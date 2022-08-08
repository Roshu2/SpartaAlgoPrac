class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        #링크드 리스트의 길이를 알아낸 다음, k만큼만 빼서 이동하면 알 수 있다
        length = 1 #시작노드의 길이
        cur = self.head

        while cur.next is not None:
            cur = cur.next
            length += 1
        end_length = length - k
        cur = self.head
        for i in range(end_length):
            cur = cur.next
        return cur


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!


def get_kth_node_from_last(self, k): #개선
    slow = self.head
    fast = self.head

    for i in range(k):
        fast = fast.next

    while fast is not None:
        slow = slow.next
        fast = fast.next

    return slow