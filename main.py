from package.controllers.AppController import AppController


class TelaExemplo:
    def mostrar_menu(self) -> None:
        print("Menu exibido")

    def mostrar_usuario(self, usuario) -> None:
        print("Usuário:", usuario.nome)
        print("Disciplinas:", [disciplina.nome for disciplina in usuario.disciplinas])

    def mostrar_erro(self, mensagem: str) -> None:
        print("Erro:", mensagem)


class RepositorioExemplo:
    def __init__(self) -> None:
        self.usuario = None

    def salvar_usuario(self, usuario) -> None:
        self.usuario = usuario

    def carregar_usuario(self):
        return self.usuario


if __name__ == "__main__":
    controller = AppController(TelaExemplo(), RepositorioExemplo())
    controller.iniciar()
    controller.adicionar_disciplina("Matemática")
    controller.adicionar_atividade("Estudar equações", "Matemática")
