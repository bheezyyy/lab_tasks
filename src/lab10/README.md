# Lab 10: Estruturas de Dados Lineares

## Descrição
Neste laboratório, foram implementadas três estruturas de dados fundamentais:
1. **Stack (Pilha)**: Segue o princípio LIFO (Last-In, First-Out). O último a entrar é o primeiro a sair.
2. **Queue (Fila)**: Segue o princípio FIFO (First-In, First-Out). O primeiro a entrar é o primeiro a sair.
3. **Singly Linked List**: Uma coleção de nós onde cada nó aponta para o próximo. Permite inserção eficiente no início.

## Teoria e Complexidade (Big O)

| Estrutura | Método | Operação | Complexidade Temporal | Motivo |
|-----------|--------|----------|-----------------------|--------|
| **Stack** | push   | Append   | O(1) | Adicionar ao fim da lista é rápido. |
| **Stack** | pop    | Pop      | O(1) | Remover do fim da lista é rápido. |
| **Queue** | enqueue| Append   | O(1) | Adicionar ao fim do deque. |
| **Queue** | dequeue| PopLeft  | O(1) | `deque` é otimizado para remover do início. `list` seria O(n). |
| **LinkedList** | prepend | Inserir Início | O(1) | Apenas ajusta ponteiros da `head`. |
| **LinkedList** | append  | Inserir Fim    | O(1)* | O(1) pois mantemos um ponteiro `tail`. Se não tivéssemos, seria O(n). |
| **LinkedList** | insert  | Inserir Meio   | O(n) | Precisa percorrer a lista até o índice. |

## Como rodar
A partir da raiz do projeto:

```bash
python main_lab10.py