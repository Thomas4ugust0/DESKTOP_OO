from __future__ import annotations

from dataclasses import dataclass

from package.models.SessaoEstudo import SessaoEstudo


@dataclass
class SessaoFocoLivre(SessaoEstudo):
    """Representa uma sessão de foco livre."""

    concluida: bool = False

    def descrever(self) -> str:
        return f"Foco livre: {self.titulo} ({self.duracao_minutos} min)"

    def concluir(self) -> None:
        self.concluida = True
