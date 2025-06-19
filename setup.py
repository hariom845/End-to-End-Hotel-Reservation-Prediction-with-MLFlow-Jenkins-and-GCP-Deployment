from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

# to run setup.py write pip install -e . in cmd
setup(
    name = "HOTEL-RESERVATION-PREDICTION",
    version = "0.1",
    author = "Hariom",
    packages= find_packages(),
    install_requires = requirements
)