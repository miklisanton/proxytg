from setuptools import setup, find_packages

setup(
    name="proxytg",
    version="0.1.0",
    author="Anton Miklis",
    author_email="antonmiklis@icloud.com",
    description="A short description of your package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/miklisanton/proxytg",
    packages=find_packages(),
    install_requires=[
        # List your package's dependencies here
        "requests>=2.32.3",
        "selenium>=4.23.1",
        "setuptools>=68.2.0",
        "selenium-wire>=5.1.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)