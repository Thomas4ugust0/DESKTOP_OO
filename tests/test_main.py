import unittest

from main import RepositorioExemplo, TelaExemplo
from package.infra.IRepository import IRepository
from package.models.Usuario import Usuario
from package.view.IView import IView


class DemoRelationsTests(unittest.TestCase):
    def test_demo_classes_implement_interfaces(self) -> None:
        self.assertTrue(issubclass(TelaExemplo, IView))
        self.assertTrue(issubclass(RepositorioExemplo, IRepository))

    def test_user_relationships_are_created_correctly(self) -> None:
        usuario = Usuario(nome="Ana")
        disciplina = usuario.adicionar_disciplina("Matemática", "Lógica")
        atividade = usuario.adicionar_atividade("Estudar equações", "Matemática")

        self.assertIn(disciplina, usuario.disciplinas)
        self.assertIn(atividade, usuario.atividades)
        self.assertIs(atividade.disciplina, disciplina)
        self.assertIn(atividade, disciplina.atividades)


if __name__ == "__main__":
    unittest.main()
