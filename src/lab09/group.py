import csv
from pathlib import Path
from typing import List
from src.lab08.models import Student

class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        self.fieldnames = ["fio", "birthdate", "group", "gpa"]
        self._ensure_storage_exists()

    def _ensure_storage_exists(self):
        """Cria o arquivo CSV e cabeçalhos se não existir."""
        if not self.path.exists():
            # Cria diretórios pais se necessário (ex: data/lab09)
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.path, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=self.fieldnames)
                writer.writeheader()

    def _read_all(self) -> List[Student]:
        """Lê todas as linhas do CSV e retorna objetos Student."""
        students = []
        if not self.path.exists():
            return students
            
        with open(self.path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    students.append(Student.from_dict(row))
                except ValueError:
                    continue # Pula linhas corrompidas
        return students

    def _save_all(self, students: List[Student]):
        """Sobrescreve o CSV com a lista atualizada de estudantes."""
        with open(self.path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writeheader()
            for s in students:
                writer.writerow(s.to_dict())

    # --- Operações CRUD Públicas ---

    def list(self) -> List[Student]:
        """READ: Retorna todos os estudantes."""
        return self._read_all()

    def add(self, student: Student):
        """CREATE: Adiciona um novo estudante ao final do arquivo."""
        # Podemos usar append mode ('a') para ser mais eficiente
        with open(self.path, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            # Se o arquivo estiver vazio (exceto header), escreve direto
            writer.writerow(student.to_dict())
        print(f"[+] Estudante adicionado: {student.fio}")

    def find(self, substr: str) -> List[Student]:
        """READ/SEARCH: Busca estudantes por substring no nome (FIO)."""
        students = self._read_all()
        results = [s for s in students if substr.lower() in s.fio.lower()]
        return results

    def remove(self, fio: str):
        """DELETE: Remove estudantes com o FIO exato."""
        students = self._read_all()
        initial_count = len(students)
        # Filtra mantendo apenas quem NÃO tem o nome a ser deletado
        students = [s for s in students if s.fio != fio]
        
        if len(students) < initial_count:
            self._save_all(students)
            print(f"[-] Estudante removido: {fio}")
        else:
            print(f"[!] Estudante não encontrado para remoção: {fio}")

    def update(self, fio: str, **fields):
        """UPDATE: Atualiza campos de um estudante existente."""
        students = self._read_all()
        updated = False
        
        for s in students:
            if s.fio == fio:
                # Atualiza os atributos passados em **fields
                for key, value in fields.items():
                    if hasattr(s, key):
                        setattr(s, key, value)
                        updated = True
        
        if updated:
            self._save_all(students)
            print(f"[*] Estudante atualizado: {fio}")
        else:
            print(f"[!] Estudante não encontrado para atualização: {fio}")

    # --- Tarefa Adicional: Estatísticas ---
    def stats(self):
        students = self._read_all()
        if not students:
            return {"count": 0}
            
        gpas = [s.gpa for s in students]
        groups = {}
        for s in students:
            groups[s.group] = groups.get(s.group, 0) + 1
            
        # Ordena por GPA descrescente para pegar o top 5
        sorted_students = sorted(students, key=lambda x: x.gpa, reverse=True)
        top_5 = [{"fio": s.fio, "gpa": s.gpa} for s in sorted_students[:5]]

        return {
            "count": len(students),
            "min_gpa": min(gpas),
            "max_gpa": max(gpas),
            "avg_gpa": sum(gpas) / len(gpas),
            "groups": groups,
            "top_5": top_5
        }