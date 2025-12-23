import dataclasses

@dataclasses.dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    # Método auxiliar para converter em dicionário (útil para CSV)
    def to_dict(self):
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }

    # Método estático para criar objeto a partir de dicionário (útil para ler CSV)
    @staticmethod
    def from_dict(data):
        return Student(
            fio=data["fio"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=float(data["gpa"])
        )