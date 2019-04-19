import setuptools

__version__ = '0.0.1'
__author__ = 'Brenner Heintz'

description = "Subtidal, for batch downloading subtitles for all movies in a media folder."

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt") as f:
    dependencies = f.read().splitlines()

setuptools.setup(
    name="subtitles",
    version=__version__,
    author=__author__,
    author_email="brennerhdata@gmail.com",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/athena15/subtidal",
    packages=['subtidal'],
    classifiers=["Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent"],
    install_requires=dependencies
)