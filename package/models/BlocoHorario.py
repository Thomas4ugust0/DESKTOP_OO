from __future__ import annotations

from dataclasses import dataclass


@dataclass
class BlocoHorario:
    """Representa um bloco de horário disponível para estudo."""

    dia_semana: str
    horario_inicio: str
    horario_fim: str

    def descrever(self) -> str:
        return f"{self.dia_semana}: {self.horario_inicio} - {self.horario_fim}"
