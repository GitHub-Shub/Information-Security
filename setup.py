# The setup.py file acts as the central configuration hub for a Machine Learning project, transforming a loose collection of scripts into a structured, installable Python package. 
# It handles project metadata like versioning and authorship while automatically managing 
# critical ML dependencies (such as scikit-learn, TensorFlow, or Pandas) to ensure 
# environment consistency. For ML engineers, its most powerful feature is enabling 
# "editable" installs (pip install -e .), which allows custom modules—like data loaders, 
# feature engineering pipelines, or model architectures—to be imported seamlessly across 
# different notebooks and scripts without manual path hacks. While modern standards 
# are shifting toward pyproject.toml, setup.py remains a staple for defining how 
# your model's code should be built, packaged, and shared.

from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """Read the requirements from a file and return them as a list."""

    requirement_lst:List[str]= []
    try:
            
        with open('requirements.txt', 'r') as file:
            lines=file.readlines()

            for line in lines:
                requirement=line.strip()

                if requirement and  requirement != '-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print(f"Requirements file was not found.")
    
    return requirement_lst

print(get_requirements())


setup(    name='Network Security',
    version='0.0.1',
    author='Shubek Sidhu',
    author_email='shubeksidhu1@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)