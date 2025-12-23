from src.lab10.structures import Stack, Queue
from src.lab10.linked_list import SinglyLinkedList

def test_stack():
    print("\n--- TESTANDO STACK (LIFO) ---")
    s = Stack()
    print("Pushing: 10, 20, 30")
    s.push(10)
    s.push(20)
    s.push(30)
    print(f"Estado atual: {s}")
    print(f"Peek (topo): {s.peek()}")
    print(f"Pop: {s.pop()}")
    print(f"Estado após pop: {s}")

def test_queue():
    print("\n--- TESTANDO QUEUE (FIFO) ---")
    q = Queue()
    print("Enqueueing: A, B, C")
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    print(f"Estado atual: {q}")
    print(f"Peek (primeiro): {q.peek()}")
    print(f"Dequeue: {q.dequeue()}")
    print(f"Estado após dequeue: {q}")

def test_linked_list():
    print("\n--- TESTANDO LINKED LIST ---")
    ll = SinglyLinkedList()
    
    print("1. Append 1, 2, 3")
    ll.append(1)
    ll.append(2)
    ll.append(3)
    print(ll)  # Saída esperada: [1] -> [2] -> [3] -> None

    print("2. Prepend 0")
    ll.prepend(0)
    print(ll)

    print("3. Insert 99 no index 2")
    ll.insert(2, 99)
    print(ll)

    print("4. Remove index 4 (o valor 3)")
    ll.remove_at(4)
    print(ll)

    print("5. Iteração:")
    for val in ll:
        print(f"Valor: {val}", end=" | ")
    print()

if __name__ == "__main__":
    test_stack()
    test_queue()
    test_linked_list()