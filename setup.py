from setuptools import find_packages, setup
from typing import List




#Declaring Variables for setup functions
PROJECT_NAME='housing-predictor'
VERSION='0.0.3'
AUTHOR="Mohammad Ansari"
DESCRIPTION="This is a first MAchine learning project"
PACKAGES= ['housing']
REQUIREMENT_FILE_NAME ='requirements.txt'
"""
Description :This function is going to return list of requirement mention in the requirement.txt file

return:THis function is going to return a list which contain name of libraries mentioned in requirements.txt file
"""

def get_requirements_list()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
name=PROJECT_NAME,
version=VERSION,
authors=AUTHOR,
description=DESCRIPTION,
packages=find_packages() ,
install_requires=get_requirements_list()


)


