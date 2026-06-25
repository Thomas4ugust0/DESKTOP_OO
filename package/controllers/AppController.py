from __future__ import annotations

from typing import TYPE_CHECKING

from package.models.Usuario import Usuario

if TYPE_CHECKING:
    from package.infra.IRepository import IRepository
    from package.view.IView import IView


class AppController:
    """Controlador principal da aplicação GoStudy."""

    def __init__(self, view: "IView", repository: "IRepository") -> None:
        self.view = view
        self.repository = repository

    def iniciar(self) -> None:
        usuario = self.repository.carregar_usuario()
        if usuario is None:
            usuario = Usuario(nome="Usuário")
            self.repository.salvar_usuario(usuario)

        self.view.mostrar_usuario(usuario)

    def adicionar_disciplina(self, nome: str, descricao: str = "") -> None:
        usuario = self.repository.carregar_usuario()
        if usuario is None:
            usuario = Usuario(nome="Usuário")

        usuario.adicionar_disciplina(nome=nome, descricao=descricao)
        self.repository.salvar_usuario(usuario)
        self.view.mostrar_usuario(usuario)

    def adicionar_atividade(self, nome: str, disciplina_nome: str) -> None:
        usuario = self.repository.carregar_usuario()
        if usuario is None:
            usuario = Usuario(nome="Usuário")

        usuario.adicionar_atividade(nome=nome, disciplina_nome=disciplina_nome)
        self.repository.salvar_usuario(usuario)
        self.view.mostrar_usuario(usuario)
