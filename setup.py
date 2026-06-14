from setuptools import find_packages, setup

def get_requirements(file_path:str) -> list[str]:
    """
    THIS FUNCTION WILL RETURN LIST OF REQUIREMENTS FROM THE REQUIREMENTS.TXT FILE
    """
    HYPEN = "-e ."
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [requirement.replace("\n", "") for requirement in requirements]

        if HYPEN in requirements:
            requirements.remove(HYPEN)
    return requirements

setup(
    name= "HYBRID HEALTHCARE RECOMMENDATION SYSTEM FOR PERSONALIZED CLINICAL TREATMENT OF DIABETES",
    version = "1.0.0",
    author = "Akahatasebhudo Emmnauel",
    author_email = "akhatasebhudoudo@gmail.com",
    description = "A healthcare recommendation system that provides personalized clinical treatment recommendations for diabetes patients based on their medical history, lifestyle, and other relevant factors.",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")
)