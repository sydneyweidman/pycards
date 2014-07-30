from setuptools import setup, find_packages

setup(
    name = "pycards",
    description = "A python-based card game framework",
    author = "Sydney Weidman",
    author_email = "sydney.weidman@gmail.com",
    packages = find_packages('src'),
    package_dir = {'':'src'},
    version="0.2",
    )
