from setuptools import setup, find_packages


HYPEN_E_DOT="-e ."

def get_requirements(filepath):
    requirements=[]
    with open(filepath,"r") as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        requirements.remove(HYPEN_E_DOT)
        return requirements


setup(
    name="Automated Job Search AI agent",
    author="Khizer, Uzair, Ramish",
    author_email="khizerkhan81009@gmali.com",
    version="0.0.1",
    packages=find_packages(),
    description="An AI-powered agent that automates the job search process.",
    install_requires=get_requirements("requirements.txt")
)