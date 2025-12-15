# python_labs/run_lab08.py
from src.lab08.models import Student
from src.lab08.serialize import students_to_json, students_from_json

# 1. Definir caminhos
input_file = "data/lab08/students_input.json"
output_file = "data/lab08/students_output.json"

print("--- 1. Lendo do JSON ---")
try:
    students = students_from_json(input_file)
    for s in students:
        print(s)
except Exception as e:
    print(f"Erro ao ler: {e}")

print("\n--- 2. Adicionando um novo aluno via Código ---")
new_student = Student(
    fio="Novo Aluno Teste", 
    birthdate="2005-01-01", 
    group="SE-03", 
    gpa=5.0
)
students.append(new_student)
print(f"Adicionado: {new_student}")

print("\n--- 3. Testando Validação (Erro Esperado) ---")
try:
    # Tentando criar aluno com nota 10 (o limite é 5)
    bad_student = Student("Erro", "2000-01-01", "A", 10.0)
except ValueError as e:
    print(f"Validação funcionou! Erro capturado: {e}")

print("\n--- 4. Salvando no arquivo de saída ---")
students_to_json(students, output_file)