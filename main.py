from package.controllers.AppController import AppController
from package.models.BlocoHorario import BlocoHorario
from package.models.Usuario import Usuario
from package.view.IView import IView
from package.infra.IRepository import IRepository


class TelaExemplo(IView):
    def mostrar_menu(self) -> None:
        print("Menu exibido")

    def mostrar_usuario(self, usuario: Usuario) -> None:
        print("Usuário:", usuario.nome)
        print("Disciplinas:", [disciplina.nome for disciplina in usuario.disciplinas])
        print("Atividades:", [atividade.nome for atividade in usuario.atividades])

    def mostrar_erro(self, mensagem: str) -> None:
        print("Erro:", mensagem)


class RepositorioExemplo(IRepository):
    def __init__(self) -> None:
        self.usuario: Usuario | None = None

    def salvar_usuario(self, usuario: Usuario) -> None:
        self.usuario = usuario

    def carregar_usuario(self) -> Usuario | None:
        return self.usuario


def executar_demonstracao() -> None:
    print("=== Demonstração das funcionalidades do GoStudy ===")

    print("\n1) Herança e polimorfismo")
    from package.models.SessaoFlashcards import SessaoFlashcards
    from package.models.SessaoFocoLivre import SessaoFocoLivre

    sessao_flashcards = SessaoFlashcards(titulo="Revisão de conceitos", duracao_minutos=20)
    sessao_flashcards.adicionar_carta_estudada("Teorema")
    sessao_foco_livre = SessaoFocoLivre(titulo="Foco profundo", duracao_minutos=45)
    sessao_foco_livre.concluir()

    for sessao in (sessao_flashcards, sessao_foco_livre):
        print(f"- {sessao.descrever()}")

    print("\n2) Composição e associação")
    usuario = Usuario(nome="Ana")
    disciplina = usuario.adicionar_disciplina("Matemática", "Lógica e cálculo")
    atividade = usuario.adicionar_atividade("Estudar equações", "Matemática")
    atividade.marcar_concluida()
    atividade.adicionar_observacao("Revisar exercícios")

    bloco = BlocoHorario(dia_semana="Segunda", horario_inicio="19:00", horario_fim="20:30")
    usuario.grade_semanal.adicionar_bloco(bloco)

    print(f"- Usuário: {usuario.nome}")
    print(f"- Disciplina: {disciplina.nome}")
    print(f"- Atividade: {atividade.nome} ({'concluída' if atividade.concluida else 'pendente'})")
    print(f"- Bloco cadastrado: {bloco.descrever()}")

    print("\n3) Dependência e uso do controller")
    controller = AppController(TelaExemplo(), RepositorioExemplo())
    controller.iniciar()
    controller.adicionar_disciplina("História", "Revolução industrial")
    controller.adicionar_atividade("Ler capítulo 1", "História")


if __name__ == "__main__":
    executar_demonstracao()
