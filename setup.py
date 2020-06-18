from setuptools import setup, find_packages

required = []

with open("requirements.txt", 'r') as f:
    required = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='db_paw',
    version='1.0',
    long_description=long_description,
    packages=find_packages(),
    install_requires=required,
)
