"""Tests for code-dependency-grapher."""
import unittest
from code_dependency_grapher.grapher import DependencyGrapher


class TestDependencyGrapher(unittest.TestCase):
    def setUp(self):
        self.g = DependencyGrapher()

    def test_import_extraction(self):
        code = "import os\nimport sys\nfrom math import sqrt\n"
        self.g.analyze_source("mod_a", code)
        deps = self.g.get_dependencies("mod_a")
        self.assertIn("os", deps)
        self.assertIn("math", deps)

    def test_cycle_detection(self):
        self.g.analyze_source("a", "import b")
        self.g.analyze_source("b", "import a")
        self.assertTrue(self.g.has_circular_dependency("a", "b"))


if __name__ == "__main__":
    unittest.main()
