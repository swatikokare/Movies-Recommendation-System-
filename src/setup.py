from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = 'SWATI'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name = SRC_REPO ,
    version= '0.0.1',
    author= AUTHOR_NAME ,
    description= ' A cloud application project',
    author_email='swatiikokare27@gmail.com',
    package = [SRC_REPO],
    python_requires = '>= 3.6',
    install_requires = [LIST_OF_REQUIREMENTS],


)
