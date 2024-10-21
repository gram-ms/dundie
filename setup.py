import os
from setuptools import setup, find_packages

def read(*paths):
    """Read the contents of a text file safely.
    >>> read("project_name", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """
    rootpath = os.path.dirname(__file__) #obtém o diretório do arquivo atual
    print(rootpath)
    filepath = os.path.join(rootpath, *paths)
    try:
        with open(filepath) as file_:
            return file_.read().strip()
    except Exception as E:
        print(f"{E}: Error ao ler arquivo txt.")

def read_requirements(path):
    """Return a list of requirements from a text file"""
    return [
        line.strip() 
        for line in read(path).split("\n")
        if not line.startswith(("#", "git+", '"', "-"))
    ]

setup(
    name="dundie",# será o nome que chamaremos com o pip ex: pip install dundie
    version="0.1.0",# sistema de versionamento
    description="Reward point system for dunder mifflin",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="EvaRgm",# autor do projeto vulgo eu
# se eu tiver pacotes em subpastas é aconcelhado utilizar o find_packages, que
# irá procurar os pacotes/módulos em todos os diretórios inclusive o atual.
# As pastas que não tiver um __init__.py serão ignoradas.
  # packages=["dundie"],# geralmente todas as pastas de módulos no seu diretório
    packages=find_packages(),
    python_requires=">=3.12.2",
    entry_points={
        "console_scripts":[
            "dundie = dundie.__main__:main"
        ]
    },
    install_requires=read_requirements("requirements.txt"),
    extras_require={
        "test": read_requirements("requirements.test.txt"),
        "dev": read_requirements("requirements.dev.txt")
    }
)
