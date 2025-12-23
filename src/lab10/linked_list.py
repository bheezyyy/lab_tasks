from typing import Any, Optional

class Node:
    """Nó da lista encadeada."""
    def __init__(self, value: Any):
        self.value = value
        self.next: Optional['Node'] = None

    def __repr__(self):
        return f"Node({self.value})"


class SinglyLinkedList:
    """
    Lista Simplesmente Encadeada.
    Possui referência para head (início) e tail (fim).
    """
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size: int = 0

    def append(self, value: Any) -> None:
        """Adiciona ao final. O(1) graças ao ponteiro tail."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self, value: Any) -> None:
        """Adiciona ao início. O(1)."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if self._size == 0:
            self.tail = new_node
        self._size += 1

    def insert(self, idx: int, value: Any) -> None:
        """Insere em um índice específico."""
        if idx < 0 or idx > self._size:
            raise IndexError("Index out of bounds")

        if idx == 0:
            self.prepend(value)
            return
        if idx == self._size:
            self.append(value)
            return

        # Caminha até o nó anterior à posição de inserção
        current = self.head
        for _ in range(idx - 1):
            current = current.next
        
        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node
        self._size += 1

    def remove_at(self, idx: int) -> None:
        """Remove o elemento no índice especificado."""
        if idx < 0 or idx >= self._size:
            raise IndexError("Index out of bounds")

        # Caso 1: Remover do início
        if idx == 0:
            self.head = self.head.next
            if self._size == 1:
                self.tail = None
            self._size -= 1
            return

        # Caso 2: Remover do meio ou fim
        current = self.head
        # Para no nó anterior ao que será deletado
        for _ in range(idx - 1):
            current = current.next
        
        # Pula o nó a ser deletado
        current.next = current.next.next

        # Se removemos o último, atualizamos o tail
        if idx == self._size - 1:
            self.tail = current

        self._size -= 1

    def __len__(self) -> int:
        return self._size

    def __iter__(self):
        """Permite usar 'for item in list'."""
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __repr__(self) -> str:
        """Visualização bonita: [1] -> [2] -> None"""
        nodes = []
        current = self.head
        while current:
            nodes.append(f"[{current.value}]")
            current = current.next
        nodes.append("None")
        return " -> ".join(nodes)