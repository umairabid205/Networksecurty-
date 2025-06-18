"""
It defines metadata, dependencies,
 and installation instructions,
 making it easier to distribute,
 install, and manage your project.
 
"""
from setuptools import setup, find_packages 

''' find_packages automatically discovers all packages and subpackages,
 whenever it found __init__.py file in the directory.
 It scans all folders in the current directory and includes them as packages.
This is useful for larger projects with multiple modules and submodules.

 '''

''' setup function is the core of the setup script.
It takes various arguments to define the package metadata,
 dependencies, and other configurations.
'''

from typing import List

def get_requirements() -> List[str]:
    """
    This function reads a file and returns a list of requirements.
    It removes any empty lines and comments starting with '#'.
    """
    requirement_lst = []

    try:
       with open('requirements.txt', 'r') as file:
           # read lines from the files
           lines = file.readlines()
           # process each line
           for line in lines:
               requirement = line.strip()
               # ignore empty lines and -e .
               if requirement and not requirement.startswith('-e .'):
                   requirement_lst.append(requirement)
    except FileNotFoundError:
       print(f"Error: The file requirements.txt was not found.")

    return requirement_lst

print(get_requirements())


setup(
    name="Network Security Project",
    version= "0.0.1",
    author= "Umair Abid",
    author_email="umairabid205@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements()

)
