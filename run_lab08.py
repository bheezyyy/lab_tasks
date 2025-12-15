import sys
import os

# Garante que o Python encontre a pasta src
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from lab08.models import Student
from lab08.serialize import students_to_json, students_from_json

# Caminhos dos arquivos
input_file = os.path.join("data", "lab08", "students_input.json")
output_file = os.path.join("data", "lab08", "students_output.json")

print("--- 1. Lendo do JSON ---")
try:
    students = students_from_json(input_file)
    for s in students:
        print(s)
except Exception as e:
    print(f"Aviso: Não foi possível ler o arquivo de entrada ({e}). Criando nova lista.")
    students = []

print("\n--- 2. Adicionando um novo aluno via Código ---")
try:
    new_student = Student(
        fio="Novo Aluno Teste", 
        birthdate="2005-01-01", 
        group="SE-03", 
        gpa=5.0
    )
    students.append(new_student)
    print(f"Adicionado: {new_student}")
except ValueError as e:
    print(f"Erro ao criar aluno: {e}")

print("\n--- 3. Testando Validação (Erro Esperado) ---")
try:
    # Tentando criar aluno com nota 10 (o limite é 5)
    bad_student = Student("Erro", "2000-01-01", "A", 10.0)
except ValueError as e:
    print(f"Sucesso! O sistema bloqueou o erro: {e}")

print("\n--- 4. Salvando no arquivo de saída ---")
students_to_json(students, output_file)
