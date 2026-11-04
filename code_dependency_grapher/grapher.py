"""Static AST dependency and import graph extractor."""
import ast
from typing import Dict, List, Set


class DependencyGrapher:
    def __init__(self):
        self._graph: Dict[str, Set[str]] = {}

    def analyze_source(self, module_name: str, code_content: str):
        if module_name not in self._graph:
            self._graph[module_name] = set()

        try:
            tree = ast.parse(code_content)
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        self._graph[module_name].add(alias.name)
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        self._graph[module_name].add(node.module)
        except SyntaxError:
            pass

    def get_dependencies(self, module_name: str) -> List[str]:
        return sorted(list(self._graph.get(module_name, set())))

    def has_circular_dependency(self, mod_a: str, mod_b: str) -> bool:
        a_deps = self._graph.get(mod_a, set())
        b_deps = self._graph.get(mod_b, set())
        return mod_b in a_deps and mod_a in b_deps
