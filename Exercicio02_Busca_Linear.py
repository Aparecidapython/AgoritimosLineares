class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, target_data, data):
        current = self.head
        while current:
            if current.data == target_data:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f"Dado alvo {target_data} não encontrado na lista.")

    def delete(self, data):
        if not self.head:
            print("Lista vazia.")
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if not current:
            print(f"Dado {data} não encontrado na lista.")
            return

        prev.next = current.next

    def display(self):
     elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Lista vazia")



if __name__ == "__main__":
    ll = LinkedList()

    ll.append(1)
    ll.append(2)
    ll.prepend(0)
    ll.insert_after(1, 1.5)

    print("Lista original:")
    ll.display()

    ll.delete(1)
    print("\nApós remover o 1:")
    ll.display()

    ll.delete(0)
    print("\nApós remover o 0:")
    ll.display()

    ll.delete(2)
    print("\nApós remover o 2:")
    ll.display()
