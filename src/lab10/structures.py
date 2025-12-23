from typing import Any, List
from collections import deque

class Stack:
    """
    Implementação de uma Pilha (Stack) usando list.
    Princípio: LIFO (Last-In, First-Out).
    """
    def __init__(self):
        self._data: List[Any] = []

    def push(self, item: Any) -> None:
        """Adiciona um item ao topo da pilha."""
        self._data.append(item)

    def pop(self) -> Any:
        """Remove e retorna o item do topo da pilha."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._data.pop()

    def peek(self) -> Any | None:
        """Retorna o item do topo sem remover. Retorna None se vazia."""
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        """Verifica se a pilha está vazia."""
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self):
        return f"Stack({self._data})"


class Queue:
    """
    Implementação de uma Fila (Queue) usando collections.deque.
    Princípio: FIFO (First-In, First-Out).
    """
    def __init__(self):
        self._data: deque = deque()

    def enqueue(self, item: Any) -> None:
        """Adiciona um item ao final da fila."""
        self._data.append(item)

    def dequeue(self) -> Any:
        """Remove e retorna o item do início da fila."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._data.popleft()  # O(1) em deque, O(n) em list

    def peek(self) -> Any | None:
        """Retorna o primeiro item sem remover. Retorna None se vazia."""
        if self.is_empty():
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        """Verifica se a fila está vazia."""
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self):
        return f"Queue({list(self._data)})"