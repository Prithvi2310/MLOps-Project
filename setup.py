from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'  #const to check if present in requirements.txt

# The following are "type hints" 
def get_requirements(file_path:str)-> List[str]:
    '''
    This function will return a list of requirements
    '''
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [chr.replace('\n',"") for chr in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements
    
setup(
    name="MLOps-Project",
    version="0.0.1",
    author="Prithvi Shah",
    author_email="shahprithvi15@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)