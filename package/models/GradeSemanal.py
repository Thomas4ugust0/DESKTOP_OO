from __future__ import annotations

from dataclasses import dataclass, field

from package.models.BlocoHorario import BlocoHorario


@dataclass
class GradeSemanal:
    """Agrupa os blocos de estudo da semana."""

    blocos: list[BlocoHorario] = field(default_factory=list)

    def adicionar_bloco(self, bloco: BlocoHorario) -> None:
        self.blocos.append(bloco)

    def listar_blocos(self) -> list[BlocoHorario]:
        return self.blocos
