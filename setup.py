from setuptools import find_packages,setup
from typing import List

def get_requiremnets(path) -> List[str]:
    requiremnets=[]
    with open(path) as file_obj:
        requiremnets=file_obj.readlines()
        requiremnets=[i.replace("\n","") for i in requiremnets]
    return requiremnets    

setup(
   name="projectml",
   version="1",
   author="sagar",
   packages=find_packages(),
   install_requires=get_requiremnets("requirements.txt")
)


