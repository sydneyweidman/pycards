from setuptools import setup, find_packages


def readme():
    return open('README.rst').read()

setup(
    name="pycards",
    version="0.2.1",
    description="A python-based card game framework",
    long_description=readme(),
    author="Sydney Weidman",
    author_email="sydney.weidman@gmail.com",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    test_suite="pycards.test",
    include_package_data=True,
)
