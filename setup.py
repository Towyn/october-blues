"""Python setup.py for october_blues package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("october_blues", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="october_blues",
    version=read("october_blues", "VERSION"),
    description="Awesome october_blues created by Towyn",
    url="https://github.com/Towyn/october-blues/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Towyn",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["october_blues = october_blues.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
