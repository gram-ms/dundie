<<<<<<< HEAD
from setuptools import setup, find_packages

setup(
    name="dundie",# será o nome que chamaremos com o pip ex: pip install dundie
    version="0.1.0",# sistema de versionamento
    description="Reward point system for dunder mifflin",
    author="EvaRgm",# autor do projeto vulgo eu
# se eu tiver pacotes em subpastas é aconcelhado utilizar o find_packages, que
# irá procurar os pacotes/módulos em todos os diretórios inclusive o atual.
# As pastas que não tiver um __init__.py serão ignoradas.
    # packages=find_packages()
    packages=["dundie"],# geralmente todas as pastas de módulos no seu diretório

)
||||||| parent of f1b8c17 (turned to installable binary #9)
=======
from setuptools import setup, find_packages

setup(
    name="dundie",# será o nome que chamaremos com o pip ex: pip install dundie
    version="0.1.0",# sistema de versionamento
    description="Reward point system for dunder mifflin",
    author="EvaRgm",# autor do projeto vulgo eu
# se eu tiver pacotes em subpastas é aconcelhado utilizar o find_packages, que
# irá procurar os pacotes/módulos em todos os diretórios inclusive o atual.
# As pastas que não tiver um __init__.py serão ignoradas.
  # packages=["dundie"],# geralmente todas as pastas de módulos no seu diretório
    packages=find_packages(),
    entry_points={
        "console_scripts":[
            "dundie = dundie.__main__:main"
        ]
    }
    
)
>>>>>>> f1b8c17 (turned to installable binary #9)
