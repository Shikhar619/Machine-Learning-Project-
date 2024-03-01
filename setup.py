from setuptools import find_packages,setup
from typing import List

hyphen = '-e .'
def get_req(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n"," ") for req in requirements]
        if hyphen in requirements:
            requirements.remove(hyphen)

    return requirements
setup(
    name = 'Machine Learning Project',
    version = '0.0.1',
    author = 'Shikhar',
    author_email= 'shikharsingh674@gmail.com',
    packages= find_packages(),
    install_requires = get_req('requirements.txt')
    
    
    )