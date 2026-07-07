from __future__ import annotations

from dataclasses import dataclass


@dataclass
class SessaoEstudo:
    """Classe base para sessões de estudo com comportamento polimórfico."""

    titulo: str
    descricao: str = ""
    duracao_minutos: int = 25

    def descrever(self) -> str:
        return f"{self.titulo} ({self.duracao_minutos} min)"
