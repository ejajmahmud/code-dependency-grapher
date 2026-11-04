"""CLI for code-dependency-grapher."""
import sys
import argparse
from .grapher import DependencyGrapher


def main():
    parser = argparse.ArgumentParser(description="Code Dependency Grapher")
    parser.add_argument("--demo", action="store_true", help="Run grapher demo")
    args = parser.parse_args()

    g = DependencyGrapher()
    g.analyze_source("auth.py", "import db\nimport util\n")
    g.analyze_source("db.py", "import config\n")
    print(f"Auth dependencies: {g.get_dependencies('auth.py')}")
    sys.exit(0)


if __name__ == "__main__":
    main()
