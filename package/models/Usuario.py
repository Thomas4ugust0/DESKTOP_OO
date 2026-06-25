from __future__ import annotations

from dataclasses import dataclass, field

from package.models.Atividade import Atividade
from package.models.Disciplina import Disciplina
from package.models.GradeSemanal import GradeSemanal
from package.models.SessaoFlashcards import SessaoFlashcards
from package.models.SessaoFocoLivre import SessaoFocoLivre


@dataclass
class Usuario:
    """Representa o usuário principal da aplicação."""

    nome: str
    disciplinas: list[Disciplina] = field(default_factory=list)
    atividades: list[Atividade] = field(default_factory=list)
    grade_semanal: GradeSemanal = field(default_factory=GradeSemanal)
    sessoes_flashcards: list[SessaoFlashcards] = field(default_factory=list)
    sessoes_foco_livre: list[SessaoFocoLivre] = field(default_factory=list)

    def adicionar_disciplina(self, nome: str, descricao: str = "") -> Disciplina:
        disciplina = Disciplina(nome=nome, descricao=descricao)
        self.disciplinas.append(disciplina)
        return disciplina

    def adicionar_atividade(self, nome: str, disciplina_nome: str) -> Atividade:
        disciplina = next((d for d in self.disciplinas if d.nome == disciplina_nome), None)
        atividade = Atividade(nome=nome, disciplina=disciplina)
        self.atividades.append(atividade)
        if disciplina is not None:
            disciplina.adicionar_atividade(atividade)
        return atividade

    def iniciar_sessao_flashcards(self, titulo: str, duracao_minutos: int = 25) -> SessaoFlashcards:
        sessao = SessaoFlashcards(titulo=titulo, duracao_minutos=duracao_minutos)
        self.sessoes_flashcards.append(sessao)
        return sessao

    def iniciar_sessao_foco_livre(self, titulo: str, duracao_minutos: int = 25) -> SessaoFocoLivre:
        sessao = SessaoFocoLivre(titulo=titulo, duracao_minutos=duracao_minutos)
        self.sessoes_foco_livre.append(sessao)
        return sessao
