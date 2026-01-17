from setuptools import setup, find_packages

setup(
    name="machine_learning",
    version="0.1.0",
    author="Aarti",
    author_email="aratideshmukh2001@gmail.com",
    packages=find_packages(),
    install_requires=["numpy", "pandas", "scikit-learn", "matplotlib", "seaborn"],
    description="A machine learning project setup"
)
