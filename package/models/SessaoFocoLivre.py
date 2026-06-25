from __future__ import annotations

from dataclasses import dataclass


@dataclass
class SessaoFocoLivre:
    """Representa uma sessão de foco livre."""

    titulo: str
    descricao: str = ""
    duracao_minutos: int = 25
    concluida: bool = False

    def concluir(self) -> None:
        self.concluida = True
