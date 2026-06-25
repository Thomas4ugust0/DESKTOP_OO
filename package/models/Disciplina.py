from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Disciplina:
    """Representa uma disciplina cadastrada pelo usuário."""

    nome: str
    descricao: str = ""
    cor: str = "#4CAF50"
    atividades: list["Atividade"] = field(default_factory=list)

    def adicionar_atividade(self, atividade: "Atividade") -> None:
        self.atividades.append(atividade)

    def __str__(self) -> str:
        return self.nome
