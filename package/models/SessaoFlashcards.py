from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class SessaoFlashcards:
    """Representa uma sessão de estudo com flashcards."""

    titulo: str
    descricao: str = ""
    duracao_minutos: int = 25
    quantidade_cartas: int = 0
    cartas_estudadas: list[str] = field(default_factory=list)

    def adicionar_carta_estudada(self, carta: str) -> None:
        self.cartas_estudadas.append(carta)
        self.quantidade_cartas += 1
