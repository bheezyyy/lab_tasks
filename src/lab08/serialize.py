import json
from pathlib import Path
from src.lab08.models import Student

def students_to_json(students: list[Student], path: str):
    """Salva uma lista de objetos Student em um arquivo JSON."""
    # 1. Converte cada objeto Student em dicionário
    data_list = [student.to_dict() for student in students]
    
    # 2. Garante que o diretório pai existe
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    # 3. Escreve no arquivo
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data_list, f, indent=4, ensure_ascii=False)
    print(f"Salvo {len(students)} estudantes em {path}")

def students_from_json(path: str) -> list[Student]:
    """Lê um arquivo JSON e retorna uma lista de objetos Student."""
    file_path = Path(path)
    
    if not file_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")

    with open(file_path, "r", encoding="utf-8") as f:
        data_list = json.load(f)

    # Converte cada dicionário do JSON de volta para um objeto Student
    students = [Student.from_dict(item) for item in data_list]
    return students