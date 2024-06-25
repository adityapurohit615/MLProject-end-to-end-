from setuptools import find_packages,setup
from typing import List

HYPEN_DOT = "-e."
def get_requirements(file_path:str)->List:


    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readline()
        requirements = [i.replace("/n","") for i in requirements]

    if HYPEN_DOT in requirements:
        requirements.remove(HYPEN_DOT)

    return requirements

setup(
    name='MLproject',
    version = '0.0.1',
    author_email='adityapurohit615@gmail.com',
    author='Aditya Purohit',
    packages = find_packages(),
    install_requires = ['numpy','pandas']


)