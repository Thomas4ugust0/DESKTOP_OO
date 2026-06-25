from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from package.models.Usuario import Usuario


class AnalistaDesempenho:
    """Responsável por avaliar o desempenho acadêmico do usuário."""

    def calcular_progresso(self, usuario: "Usuario") -> dict[str, int]:
        total_atividades = len(usuario.atividades)
        concluídas = sum(1 for atividade in usuario.atividades if atividade.concluida)

        return {
            "total_atividades": total_atividades,
            "concluidas": concluídas,
            "percentual": int((concluídas / total_atividades * 100) if total_atividades else 0),
        }

    def resumir(self, usuario: "Usuario") -> str:
        dados = self.calcular_progresso(usuario)
        return (
            f"{usuario.nome}: {dados['concluidas']}/{dados['total_atividades']} atividades concluídas "
            f"({dados['percentual']}%)"
        )
