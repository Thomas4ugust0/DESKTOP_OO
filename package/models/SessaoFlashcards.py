from __future__ import annotations

from dataclasses import dataclass, field

from package.models.SessaoEstudo import SessaoEstudo


@dataclass
class SessaoFlashcards(SessaoEstudo):
    """Representa uma sessão de estudo com flashcards."""

    quantidade_cartas: int = 0
    cartas_estudadas: list[str] = field(default_factory=list)

    def descrever(self) -> str:
        return f"Flashcards: {self.titulo} ({self.duracao_minutos} min)"

    def adicionar_carta_estudada(self, carta: str) -> None:
        self.cartas_estudadas.append(carta)
        self.quantidade_cartas += 1
