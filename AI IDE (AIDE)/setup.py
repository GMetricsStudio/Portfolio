# setup.py
from setuptools import setup, find_packages

setup(
    name="ai-dev-ide",
    version="2.0.0",
    packages=find_packages(),
    install_requires=[
        "huggingface-hub>=0.20.0",
        "requests>=2.31.0",
        "pygments>=2.16.1",
        "pytest>=7.4.0",
        "coverage>=7.3.0",
    ],
    python_requires=">=3.8",
)