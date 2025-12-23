from src.lab08.models import Student
from src.lab09.group import Group

def main():
    # Caminho onde o CSV será salvo
    db_path = "data/lab09/students.csv"
    
    # 1. Inicializa o Grupo (Cria o arquivo se não existir)
    group_db = Group(db_path)
    print("=== Banco de dados inicializado ===")

    # 2. CREATE: Adicionar estudantes
    s1 = Student("Ivanov Ivan", "2003-10-10", "BIVT-21-1", 4.3)
    s2 = Student("Petrov Petr", "2002-05-15", "BIVT-21-2", 3.8)
    s3 = Student("Sidorova Anna", "2004-01-20", "BIVT-21-1", 4.9)
    
    group_db.add(s1)
    group_db.add(s2)
    group_db.add(s3)

    # 3. READ: Listar todos
    print("\n=== Lista de Estudantes ===")
    for s in group_db.list():
        print(s)

    # 4. UPDATE: Atualizar GPA do Ivanov
    print("\n=== Atualizando Ivanov ===")
    group_db.update("Ivanov Ivan", gpa=5.0)
    
    # 5. FIND: Buscar por substring
    print("\n=== Buscando 'Anna' ===")
    found = group_db.find("Anna")
    print(found)

    # 6. DELETE: Remover Petrov
    print("\n=== Removendo Petrov ===")
    group_db.remove("Petrov Petr")

    # 7. Verificação Final e Stats
    print("\n=== Estatísticas Finais ===")
    stats = group_db.stats()
    import json
    print(json.dumps(stats, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()