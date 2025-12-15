from dataclasses import dataclass
from datetime import datetime, date

@dataclass
class Student:
    fio: str          # Nome completo
    birthdate: str    # Data no formato "YYYY-MM-DD"
    group: str        # Ex: "SE-01"
    gpa: float        # Nota média (0 a 5)

    def __post_init__(self):
        """
        Validação automática executada após a criação do objeto.
        """
        # 1. Validação do formato da data (YYYY-MM-DD)
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Data inválida: {self.birthdate}. Use o formato YYYY-MM-DD.")

        # 2. Validação do GPA (0 a 5)
        if not (0 <= self.gpa <= 5):
            raise ValueError(f"GPA inválido: {self.gpa}. Deve estar entre 0 e 5.")

    def age(self) -> int:
        """Calcula a idade baseada na data de hoje."""
        today = date.today()
        bdate = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        
        # Subtrai os anos e ajusta se o aniversário ainda não ocorreu este ano
        age = today.year - bdate.year - ((today.month, today.day) < (bdate.month, bdate.day))
        return age

    def to_dict(self) -> dict:
        """Converte o objeto Student para um dicionário (útil para JSON)."""
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Cria um objeto Student a partir de um dicionário."""
        return cls(
            fio=data["fio"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=data["gpa"]
        )

    def __str__(self):
        """Representação bonita em texto para o print()."""
        return f"Student(Nome: {self.fio}, Grupo: {self.group}, Média: {self.gpa}, Idade: {self.age()})" 