import unittest
import json
import os


class TestTrilhasJSON(unittest.TestCase):

    def setUp(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.json_path = os.path.join(base_dir, "data", "trilhas.json")

    def test_arquivo_carrega_corretamente(self):
        with open(self.json_path, "r", encoding="utf-8") as f:
            dados = json.load(f)
        self.assertIsInstance(dados, dict)
        self.assertIn("trilhas", dados)

    def test_contem_tecnologia_python(self):
        with open(self.json_path, "r", encoding="utf-8") as f:
            dados = json.load(f)
        tecnologias = [t["tecnologia"] for t in dados["trilhas"]]
        self.assertIn("Python", tecnologias)


if __name__ == "__main__":
    unittest.main()
