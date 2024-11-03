from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str)->List[str]:
    requirement = []
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [(req.replace("\n,", "")) for req in requirement]
        if HYPHEN_E_DOT in requirement:
            requirement.remove(HYPHEN_E_DOT)

        return requirement



setup(
    name= "Cat_v_Dog Classification",
    version= "0.0.1",
    author = "Khizar Abbasi",
    author_email= "Khizerabbasi144@gamil.com",
    packages= find_packages(),
    install_require = get_requirements("requirements.txt"),
)