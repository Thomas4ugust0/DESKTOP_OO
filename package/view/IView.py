from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from package.models.Usuario import Usuario


class IView(ABC):
    """Interface para a camada de visualização."""

    @abstractmethod
    def mostrar_menu(self) -> None:
        """Exibe o menu principal da aplicação."""

    @abstractmethod
    def mostrar_usuario(self, usuario: "Usuario") -> None:
        """Exibe os dados do usuário."""

    @abstractmethod
    def mostrar_erro(self, mensagem: str) -> None:
        """Exibe uma mensagem de erro para o usuário."""
