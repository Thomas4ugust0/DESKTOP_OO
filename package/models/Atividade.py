from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from package.models.BlocoHorario import BlocoHorario
from package.models.Disciplina import Disciplina


@dataclass
class Atividade:
    """Representa uma atividade de estudo vinculada a uma disciplina."""

    nome: str
    disciplina: Optional[Disciplina] = None
    bloco_horario: Optional[BlocoHorario] = None
    concluida: bool = False
    observacoes: list[str] = field(default_factory=list)

    def marcar_concluida(self) -> None:
        self.concluida = True

    def adicionar_observacao(self, observacao: str) -> None:
        self.observacoes.append(observacao)
