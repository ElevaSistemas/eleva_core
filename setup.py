from pathlib import Path
from setuptools import setup, find_packages

requirements = Path("requirements.txt").read_text().splitlines() if Path("requirements.txt").exists() else []
version = {}
exec(Path("eleva_core/__init__.py").read_text(), version)

setup(
    name="eleva_core",
    version=version["__version__"],
    description="Modulo 1 - Cadastros e Controles da Eleva em Frappe",
    author="Eduardo Vessio / OpenAI",
    author_email="eduardovessio@hotmail.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=requirements,
)
