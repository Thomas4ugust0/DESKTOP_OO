from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from package.models.Usuario import Usuario


class IRepository(ABC):
    """Interface para persistência dos dados do usuário."""

    @abstractmethod
    def salvar_usuario(self, usuario: "Usuario") -> None:
        """Salva ou atualiza o estado do usuário."""

    @abstractmethod
    def carregar_usuario(self) -> "Usuario | None":
        """Carrega o usuário salvo, caso exista."""
